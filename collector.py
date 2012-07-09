#!/usr/bin/env python

import sys
import datetime
import logging
import traceback

import tweepy

from mkondo import gmailer,gatherer,tweetstream

def collect(settings):
	mailer = gmailer.Gmailer(settings.get('GMAIL_USER'), settings.get('GMAIL_PASSWORD'))
	message = "Starting collection at:  %s, %s" % (datetime.datetime.now(), settings.get('APP_ID'))	
	mailer.send_gmail(settings.get('OPS_EMAILS'), "Collection started: %s" % settings.get('APP_ID'), message)

	#Rotate files more frequently
	data_log_path = settings.get('DATA_DIRECTORY') + settings.get('DATA_LOG_NAME')
	app_log_path = settings.get('APP_LOG_DIRECTORY') + settings.get('APP_LOG_NAME')
	stream_listener = gatherer.TwitterStreamListener(data_log_path, app_log_path, 'M', 15)

	logger = logging.getLogger(gatherer.LoggingConfig.APP_LOG)
	logger.info(message)

	try:
		auth = tweepy.BasicAuthHandler(settings.get('TWITTER_USERNAME'), settings.get('TWITTER_PASSWORD'))
		stream = tweetstream.CompliantStream(auth, stream_listener, 5, stream_log_name=settings.get('STREAM_LOG_NAME'))
		stream.filter(track=settings.get('KEYWORDS'))

	# The exception handling is pretty heavy here. Issues happen infrequently, so any information 
	# we can get is useful. 
	except Exception as exception:
		trace = traceback.format_exc()
		message = "Keyword collection terminated at: %s reason: %s, %s" % (datetime.datetime.now(), 
					trace, settings.get('APP_ID'))

		logger.exception(message)
		mailer.send_gmail(settings.get('OPS_EMAILS'), 'Exception %s' % settings.get('APP_ID'), message) 
	except:
		trace = traceback.format_exc()
		message = "Keyword collection terminated with empty exception at: %s reason: %s, %s " % (datetime.datetime.now(), 
					trace, settings.get('APP_ID'))
		logger.exception(message)
		mailer.send_gmail(settings.get('OPS_EMAILS'), 'Empty Exception: %s' % settings.get('APP_ID'), message)
		raise
	else:
		message = "Application terminated at: %s. No exception. %s" % (datetime.datetime.now(), settings.get('APP_ID'))
		logger.error(message)
		mailer.send_gmail(settings.get('OPS_EMAILS'), 'No Exception: %s' % settings.get('APP_ID'), message)
