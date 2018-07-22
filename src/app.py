from __future__ import print_function

import json

def lambda_handler(event, context):
    print("Event Passed to Handler: " + json.dumps(event))
    body = json.loads(event['body'])
    return {
        "statusCode": 200,
        "body": json.dumps({
            'message': 'hello world',
            'location': body,
        })
    }