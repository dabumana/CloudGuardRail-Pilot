import boto3
import json
import os

sns = boto3.client('sns')
sqs = boto3.client('sqs')

def handle(event, context):
    check_attr(event)
    send_msg(event)

def check_attr(event):
    topic = os.environ['TopicArn']
    queueUrl = event['detail']['requestParameters']['queueUrl']
    tags = ['Name','Created By','Cost Center']
    
    vpc_attr = sqs.get_queue_attributes(
        QueueUrl = queueUrl,
        AttributeNames = ['VPC']['Attributes']['VPC'])
    if not vpc_attr:
        publish_event(topic, vpc_attr)
    
    kms_attr = sqs.get_queue_attributes(
        QueueUrl = queueUrl,
        AttributeNames = ['KmsMasterKeyId']['Attributes']['KmsMasterKeyId'])
    if not kms_attr:
        publish_event(topic, kms_attr)
    
    tag_list = sqs.list_queue_tags(QueueUrl=queueUrl)['Tags']
    for i in tags:
        if i not in tag_list:
            publish_event(topic, tag_list)
            break

def publish_event(topic, msg):
    sns.publish(
        TopicArn=topic,
        Message=f"{msg}",
        Subject='Test Message'
    )

def send_msg(event):
    sqs.send_message(
        QueueUrl = event['detail']['requestParameters']['queueUrl'],
        MessageBody = json.dumps(event)
    )
