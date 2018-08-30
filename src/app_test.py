from app import lambda_handler

def test_app_lambda_handler():

  event = {
    'queryStringParameters': {
      'name': 'testname'
    }
  }

  context = {}

  expected = {
    'body': '{"message": "Hello testname"}',
    'statusCode': 200
  }

  assert lambda_handler(event, context) == expected