import os

# Default app config
AWS_REGION = 'us-west-2'
FLASK_DEBUG = 'true'
SOURCE_EMAIL_ADDRESS = 'nobody@amazon.com'

LOGGING_LEVEL = os.environ['LOGGING_LEVEL'] if 'LOGGING_LEVEL' in os.environ else 'DEBUG'
