from __future__ import print_function

import json

def lambda_handler(event, context):
    print("Event Passed to Handler: " + json.dumps(event)) 
    name = 'world'
    if event['queryStringParameters'] is not None:
      name = event['queryStringParameters']['name']

    return {
        "statusCode": 200,
        "body": json.dumps({
            'message': 'Hello '+name
        })
    }