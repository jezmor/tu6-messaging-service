import os
import boto3
import json
import logging
from twilio.rest import Client
from botocore.exceptions import ClientError

root = logging.getLogger()
if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)


def get_twilio_credentials():
    secret_name = "twilio_credentials"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        logging.debug("Getting secret values from SecretsManager...")
        secret_values = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        logging.critical("Failed to retrieve secret values from SecretsManager.")
        raise e

    logging.debug("Successfully retrieved secret values from SecretsManager.")
    return json.loads(secret_values['SecretString'])

def twilio_send_message(to,msg):
    #https://www.twilio.com/docs/usage/api?code-sample=code-send-a-simple-sms-using-the-programmable-sms-api&code-language=Python&code-sdk-version=7.x
    credentials = get_twilio_credentials()

    account_sid = credentials['TWILIO_ACCOUNT_SID']
    auth_token = credentials['TWILIO_AUTH_TOKEN']
    twilio_number = os.environ['TWILIO_NUMBER']

    client = Client(account_sid, auth_token)

    try:
        logging.debug(f"Sending Twilio message from {account_sid} to {twilio_number}.\nMessage Content:\n{msg}")
        message = client.messages \
            .create(
                body=msg,
                from_=twilio_number,
                to=to
            )
    except ClientError as e:
        logging.critical(f"Failed to send Twilio text message from {account_sid} to {twilio_number}.\nMessage Content:\n{msg}\nFailure Reason:\n{e}")
        raise e

    return message


def lambda_handler(event, context):
    for message in event['Records']:
        try:
            logging.debug("Gathering SQS message body...")
            item = json.loads(message['body'])
        except ValueError as e:
            logging.critical(f"Unable to parse SQS message body, improper JSON.\nSQS Message Body: \n{message['body']}")
            raise e

        to = item['to']
        msg = item['msg']+"\nReply STOP to stop receiving these messages."

        try:
            twl = twilio_send_message(to,msg)
            
            if twl.account_sid:
                return {
                    'statusCode': 200,
                    'body': f"SUCCESS! account_sid={twl.account_sid} sid={twl.sid}"
                }
        except Exception as e:
            logging.critical(f"TWILIO ERROR: {e}")
            raise e