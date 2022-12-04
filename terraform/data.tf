data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

data "aws_secretsmanager_secret" "twilio_credentials" {
  name = "twilio_credentials"
}

data "aws_secretsmanager_secret_version" "twilio_credentials_current" {
  secret_id = data.aws_secretsmanager_secret.twilio_credentials.id
}


resource "null_resource" "copy_lambda_function_into_zip" {
  provisioner "local-exec" {
    command = "zip lambda_function.zip ../lambda/lambda_function.py -j"
  }
}

resource "null_resource" "copy_lambda_layers_into_zip" {
  provisioner "local-exec" {
    command = "cd ../lambda && zip ../terraform/sendtext_lambda_layers.zip ./python -r; cd ../terraform"
  }
}