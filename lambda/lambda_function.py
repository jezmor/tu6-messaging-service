import os
import boto3
import json
import logging
from twilio.rest import Client
from botocore.exceptions import ClientError

#https://aws.amazon.com/blogs/mt/get-notified-specific-lambda-function-error-patterns-using-cloudwatch/
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger(__name__)

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
        secret_values = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    return json.loads(secret_values['SecretString'])

def twilio_send_message(to,msg):
    #https://www.twilio.com/docs/usage/api?code-sample=code-send-a-simple-sms-using-the-programmable-sms-api&code-language=Python&code-sdk-version=7.x
    credentials = get_twilio_credentials()

    account_sid = credentials['TWILIO_ACCOUNT_SID']
    auth_token = credentials['TWILIO_AUTH_TOKEN']
    twilio_number = os.environ['TWILIO_NUMBER']

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=msg,
            from_=twilio_number,
            to=to
        )

    return message


def lambda_handler(event, context):
    for message in event['Records']:
        item = json.loads(message['body'])

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
            print(e)
            logger.critical(f"TWILIO ERROR: {e}")
            
            return {
                'statusCode': 500,
                'body': f"FAILED! {e}"
            }