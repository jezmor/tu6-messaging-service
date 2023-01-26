data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

data "aws_secretsmanager_secret" "twilio_credentials" {
  name = "twilio_credentials"
}

data "aws_secretsmanager_secret_version" "twilio_credentials_current" {
  secret_id = data.aws_secretsmanager_secret.twilio_credentials.id
}

data "archive_file" "zip_lambda_function" {
  type = "zip"
  source_file = "../lambda/lambda_function.py"
  output_path = "sendtext_lambda_function.zip"
}

data "archive_file" "zip_lambda_layers" {
  type = "zip"
  source_dir = "../lambda/python/"
  output_path = "sendtext_lambda_layers.zip"
}