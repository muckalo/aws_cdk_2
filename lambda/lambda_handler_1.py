"""
Lambda Module
"""

import json


def lambda_handler(event, context):
    """
    Lambda Handler

    :param event:
    :param context:
    :return:
    """

    print(f'event: {type(event)} - {event}')

    for record in event['Records']:
        sns_msg = record['Sns']['Message']
        print(f'sns_msg: {type(sns_msg)} - {sns_msg}')

        s3_event = json.loads(sns_msg)
        for s3_record in s3_event['Records']:
            bucket_name = s3_record['s3']['bucket']['name']
            object_key = s3_record['s3']['object']['key']
            print(f'Object "{object_key} successfully inserted into bucket "{bucket_name}"')

    return {
        'statusCode': 200,
        'body': json.dumps('Finished lambda_handler')
    }
