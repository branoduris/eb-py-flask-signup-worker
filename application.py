# Copyright 2013. Amazon Web Services, Inc. All Rights Reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

import logging
import logging.handlers
import json

import flask
from flask import request, Response

import boto.ses

# Create and configure the Flask app
application = flask.Flask(__name__)
application.config.from_object('default_config')
application.debug = application.config['FLASK_DEBUG'] in ['true', 'True']


# # Create logger
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# # Handler
# LOG_FILE = '/opt/python/log/tcw-app.log'
# # handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
# handler = logging.handlers.logging.StreamHandler(sys.stdout)
# handler.setLevel(logging.INFO)
#
# # Formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# # Add Formatter to Handler
# handler.setFormatter(formatter)
#
# # add Handler to Logger
# logger.addHandler(handler)


logging.basicConfig(level=application.config['LOGGING_LEVEL'])

@application.route('/customer-registered', methods=['POST'])
def customer_registered():
    """Send an e-mail using SES"""



    response = None
    if request.json is None:
        # Expect application/json request
        response = Response("", status=415)
    else:
        # message = dict()
        try:
            # If the message has an SNS envelope, extract the inner message
            if 'TopicArn' in request.json and 'Message' in request.json:
                message = json.loads(request.json['Message'])
            else:
                message = request.json

            logging.debug("Received message: %s" % message)
            logging.debug("Headers: %s" % request.headers)
        #
        #     # Connect to SES and send an e-mail
        #     ses = boto.ses.connect_to_region(application.config['AWS_REGION'])
        #     ses.send_email(source=application.config['SOURCE_EMAIL_ADDRESS'],
        #                    subject=SUBJECT,
        #                    body=BODY % (message['name']),
        #                    to_addresses=[message['email']])
            response = Response("", status=200)
        except Exception as ex:
            logging.exception('Error processing message: %s' % request.json)
            response = Response(ex.message, status=500)

    return response


@application.route('/test-scheduled', methods=['POST'])
def test_scheduled():
    logging.info("Scheduled task called")

    # logging.debug("Received request: %s" % request)
    #
    # if request.json is not None:
    #     logging.debug("Received message: %s" % request.json)
    logging.debug("Headers: %s" % request.headers)

    return Response("", status=200)

if __name__ == '__main__':
    application.run(host='0.0.0.0')
