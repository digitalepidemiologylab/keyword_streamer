import keywords 

# Gmail account information for the system to send email as. 
GMAIL_USER = ''
GMAIL_PASSWORD = ''

OPS_EMAILS = ['khandelwal@gmail.com']

APP_ID = 'Crowdbreaks Keyword Search'

#DATA_DIRECTORY must have trailing slash. 
DATA_DIRECTORY = '/opt/code/twitter-keywords/data/'
DATA_LOG_NAME = 'data.log' 

CATCHUP_DATA_LOG_NAME = 'catchup.log'

COLLECTOR_APP_LOG_NAME = 'collector-app.log'
COLLECTOR_DATA_LOG_NAME = 'collector-data.log'

#APP_LOG_DIRECTORY must have trailing slash. 
APP_LOG_DIRECTORY = '/opt/code/twitter-locations/data/raw-app-logs/'
APP_LOG_NAME =  'app.log'
STREAM_LOG_NAME =  'stream.log'

KEYWORDS = ['flu', 'influenza', 'fever', 'headache', 'sore throat',
	'sorethroat', 'sick', 'chills', 'cough', 'coughing', 'h1n1', 'swine flu',
	'swineflu', 'flu shot', 'flushot', 'vaccine', 'vaccination', 'vaccinated',
	'immunized', 'immunization', 'vaccinating', 'immunizing', 'vaccinate',
	'immunize', 'shingles', 'ppsv', 'autism', 'autistic', 'zoster', 'chickenpox',
	'diptheria', 'measles', 'mumps', 'pertussis', 'polio', 'pneumococcal',
	'rotavirus', 'rubella', 'tetanus', 'hepb', 'dtap', 'hib', 'pcv', 'ipv', 'mmr',
	'varicella', 'hepa', 'papillomavirus', 'tdap', 'hpv', 'hepatitis', 'mcv4', 'h5n1', 'h3n2', 'h1n2',
	'antibiotic', 'antibiotics', 'zpack', 'z pack', 'z-pack', 'zpac', 'z pac', 'z-pac', 
	'herpes', 'meningitis', 'ecoli', 'ehec', 'e. coli', 'ndm1', 'ndm-1']

KEYWORDS = [item for sublist in keywords.KEYWORDS.values() for item in sublist]

TWITTER_USERNAME = ''
TWITTER_PASSWORD = ''

AWS_ACCESS_KEY=''
AWS_SECRET_KEY=''
AWS_BACKUP_BUCKET = 'crowdbreaks-tweets-salathegroup'

OAUTH_CONSUMER_TOKEN = ''
OAUTH_CONSUMER_SECRET = ''
OAUTH_ACCESS_TOKEN = ''
OAUTH_ACCESS_TOKEN_SECRET = ''

#The name of the sub-directory that the backup program puts backed up files in. 
BACKUP_DIR = 'SB_DATA_SB'

# To override the above settings (in production, etc) create a file called local.py that contains deployment 
# specific values. 

try:
	# Pull in the local changes
	from local_settings import * 
except ImportError:
	pass
