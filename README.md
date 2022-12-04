# tu6-messaging-service
Serverless Text Messaging

## Welcome!

This project simplifies text messaging from web apps!

## Getting Setup
1. Configure Twilio
- Create an account with (Twilio)[https://www.twilio.com/try-twilio].
- Buy a phone number
- Save your ACCOUNT_SID and ACCOUNT_AUTH_TOKEN in (AWS SecretsManager)[https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html] in US-EAST-1 as "twilio_credentials"
2. (Configure the AWS CLI)[https://aws.amazon.com/cli/]
3. Create an S3 Bucket to Host your .tfstate file
4. Modify the Terraform Backend Command with your S3 state file location
5. Run `terraform init` and `terraform apply` insert the phone number you just created in TWILIO_NUMBER variable!
- Alternatively you can use `terraform apply -var TWILIO_NUMBER="+19999999999`<- Replace with your Twilio Number.

## Using the Service
In order to send/receive messages you'll have to send messages into the text-messages sqs queue. The expected format is
```
{
"msg":"Hello World! Your Message Here!",
"to":"+19999999999"
}
```

When entering your phone number, be sure to add **+1** before the number! Happy texting!
