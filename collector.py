#!/usr/bin/env python

import sys
import settings
import datetime
import logging
import traceback

import tweepy

from mkondo import gmailer,gatherer,tweetstream

def main():
	mailer = gmailer.Gmailer(settings.GMAIL_USER, settings.GMAIL_PASSWORD)
	message = "Starting collection at:  %s, %s" % (datetime.datetime.now(), settings.APP_ID)	
	mailer.send_gmail(settings.OPS_EMAILS, "Collection started: %s" % settings.APP_ID, message)

	#Rotate files more frequently
	data_log_path = settings.DATA_DIRECTORY + settings.DATA_LOG_NAME
	app_log_path = settings.APP_LOG_DIRECTORY + settings.APP_LOG_NAME
	stream_listener = gatherer.TwitterStreamListener(data_log_path, app_log_path, 'M', 15)

	logger = logging.getLogger(gatherer.LoggingConfig.APP_LOG)
	logger.info(message)

	try:
		auth = tweepy.BasicAuthHandler(settings.TWITTER_USERNAME, settings.TWITTER_PASSWORD)
		stream = tweetstream.CompliantStream(auth, stream_listener, 5, stream_log_name=settings.STREAM_LOG_NAME)
		stream.filter(track=settings.KEYWORDS)

	# The exception handling is pretty heavy here. Issues happen infrequently, so any information 
	# we can get is useful. 
	except Exception as exception:
		trace = traceback.format_exc()
		message = "Keyword collection terminated at: %s reason: %s, %s" % (datetime.datetime.now(), 
					trace, settings.APP_ID)

		logger.exception(message)
		mailer.send_gmail(settings.OPS_EMAILS, 'Exception %s' % settings.APP_ID, message) 
	except:
		trace = traceback.format_exc()
		message = "Keyword collection terminated with empty exception at: %s reason: %s, %s " % (datetime.datetime.now(), 
					trace, settings.APP_ID)
		logger.exception(message)
		mailer.send_gmail(settings.OPS_EMAILS, 'Empty Exception: %s' % settings.APP_ID, message)
		raise
	else:
		message = "Application terminated at: %s. No exception. %s" % (datetime.datetime.now(), settings.APP_ID)
		logger.error(message)
		mailer.send_gmail(settings.OPS_EMAILS, 'No Exception: %s' % settings.APP_ID, message)

if __name__ == '__main__':
	main()
