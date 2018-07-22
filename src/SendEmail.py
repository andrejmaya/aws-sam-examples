
import boto3
import json
from botocore.exceptions import ClientError


def lambda_handler(event, context):

    email_from = 'andrejmaya@googlemail.com'
    email_to = 'info@mayasoft.de'
    
    requestData = event
    if 'body' in event:
       requestData=event['body']
    requestData = json.dumps(requestData)
    print(requestData)
    
    ses = boto3.client('ses',region_name="eu-west-1")
    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = ses.send_email(
            Destination={
                'ToAddresses': [
                    email_to,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': requestData,
                    },
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': requestData,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': "contact request from your website",
                },
            },
            Source=email_from,
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'statusCode': 500, 'body': 'error', 'isBase64Encoded': 0,'headers':{}}
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
        return {'statusCode': 200, 'body': 'success', 'isBase64Encoded': 0,'headers':{}}