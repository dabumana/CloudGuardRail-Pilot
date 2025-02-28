import boto3
import json
import os

def handler(event, context):
    print('Received event:', event)
    sns = boto3.client('sns')
    sns.publish(
        TopicArn=os.environ['TopicArn'],
        Message='Hello from hell!!!',
        Subject='Test Message'
    )
    return {
       'statusCode': 200,
        'body': json.dumps('Hello from hell!!!')
    }
