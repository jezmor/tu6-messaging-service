resource "aws_budgets_budget" "textMailingListService" {
  name              = "text-message-service-budget"
  budget_type       = "COST"
  limit_amount      = "100.00"
  limit_unit        = "USD"
  time_unit         = "MONTHLY"
  time_period_start = "2022-12-03_00:01"
}

resource "aws_iam_role" "lambda_execution_role_sendtxt" {
  name = "lamdarole-sendtext"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_policy_attachment" "attach_cw_policies_lambda_sendtext_role" {
  name       = "attach-cloudwatch-policy"
  policy_arn = aws_iam_policy.lambda_sendText_cloudwatch_policy.arn
  roles      = [aws_iam_role.lambda_execution_role_sendtxt.name]
}

resource "aws_iam_policy_attachment" "attach_sqs_policies_lambda_sendtext_role" {
  name       = "attach-sqs-policy"
  policy_arn = aws_iam_policy.lambda_sendText_sqs_policy.arn
  roles      = [aws_iam_role.lambda_execution_role_sendtxt.name]
}

resource "aws_iam_policy_attachment" "attach_sm_policies_lambda_sendtext_role" {
  name       = "attach-sm-policy"
  policy_arn = aws_iam_policy.lambda_twilio_credentials_policy.arn
  roles      = [aws_iam_role.lambda_execution_role_sendtxt.name]
}

resource "aws_iam_policy" "lambda_sendText_cloudwatch_policy" {
  name        = "lambda_send_text_cloudwatch"
  path        = "/text-message-service/lambda/policies/"
  description = "iam role for sendText lambda to CloudWatch"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "logs:CreateLogGroup",
        ]
        Effect   = "Allow"
        Resource = "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:*"
      },
      {
        Action = [
          "logs:CreateLogStream",
          "logs:PutLogEvents",
        ]
        Effect   = "Allow"
        Resource = "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${aws_lambda_function.lambda_sendtext.function_name}:*"
      }
    ]
  })
}

resource "aws_iam_policy" "lambda_twilio_credentials_policy" {
  name        = "lambda_twilio_credentials_policy"
  path        = "/text-message-service/lambda/policies/"
  description = "iam role for sendText lambda to access twilio credentials"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "secretsmanager:GetSecretValue",
        ]
        Effect   = "Allow"
        Resource = data.aws_secretsmanager_secret.twilio_credentials.arn
      }
    ]
  })
}

resource "aws_iam_policy" "lambda_sendText_sqs_policy" {
  name        = "lambda_send_text_sqs"
  path        = "/text-message-service/lambda/policies/"
  description = "iam role for sendText lambda to CloudWatch"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "sqs:DeleteMessage",
          "sqs:GetQueueUrl",
          "sqs:ListDeadLetterSourceQueues",
          "sqs:ChangeMessageVisibility",
          "sqs:ReceiveMessage",
          "sqs:GetQueueAttributes",
        ],
        Effect   = "Allow"
        Resource = aws_sqs_queue.sqs-text-messages.arn
      }
    ]
  })
}

resource "aws_sqs_queue" "sqs-text-messages" {
  name                       = "text-messages"
  delay_seconds              = 90
  max_message_size           = 2048
  message_retention_seconds  = 345600
  receive_wait_time_seconds  = 0
  visibility_timeout_seconds = 600

}

resource "aws_lambda_function" "lambda_sendtext" {
  function_name    = "sendtext"
  filename         = "lambda_function.zip"
  source_code_hash = filebase64sha256("lambda_function.zip")
  role             = aws_iam_role.lambda_execution_role_sendtxt.arn
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.7"
  timeout          = 180
  layers           = [aws_lambda_layer_version.sendtext_lambda_layer.arn]
  depends_on       = [null_resource.copy_lambda_function_into_zip]

  environment {
    variables = {
      TWILIO_NUMBER = var.TWILIO_NUMBER
    }
  }
}

resource "aws_lambda_layer_version" "sendtext_lambda_layer" {
  filename                 = "sendtext_lambda_layers.zip"
  layer_name               = "python_twilio_7-15-4"
  compatible_runtimes      = ["python3.7"]
  compatible_architectures = ["x86_64"]

  depends_on = [null_resource.copy_lambda_layers_into_zip]
}

resource "aws_lambda_event_source_mapping" "sqs_trigger_sendtext" {
  event_source_arn = aws_sqs_queue.sqs-text-messages.arn
  function_name    = aws_lambda_function.lambda_sendtext.function_name
}