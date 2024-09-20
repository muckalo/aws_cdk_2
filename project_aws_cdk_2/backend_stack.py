"""
Backend Stack Module
"""

from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_ec2 as ec2,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_s3 as s3,
    aws_s3_notifications as s3n,
    aws_dynamodb as ddb,
    RemovalPolicy
)
from constructs import Construct


class BackendStack(Stack):
    """
    Backend Stack
    """

    def __init__(self, scope: Construct, _id: str, vpc: ec2.Vpc, table=ddb.Table, **kwargs) -> None:
        super().__init__(scope, _id, **kwargs)

        part = '2'

        my_lambda = _lambda.Function(
            self,
            f'lambda-id-{part}',
            function_name=f"lambda-{part}",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='lambda_handler_1.lambda_handler',
            code=_lambda.Code.from_asset('lambda'),
            vpc=vpc,
            environment={
                'TABLE_NAME': table.table_name
            }
        )

        table.grant_read_write_data(my_lambda)

        my_topic = sns.Topic(
            self,
            f'sns-topic-id-{part}',
            topic_name=f'sns-topic-{part}',
            display_name=f'sns-topic-display-name-{part}'
        )
        my_topic.add_subscription(subs.LambdaSubscription(my_lambda))

        my_bucket = s3.Bucket(
            self,
            f'bucket-backend-id-{part}',
            bucket_name=f'bucket-backend-{part}',
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,  # Removes the bucket when the stack is deleted
            block_public_access=s3.BlockPublicAccess(
                block_public_acls=False,
                ignore_public_acls=False,
                block_public_policy=False,
                restrict_public_buckets=False
            ),  # This disables blocking
            public_read_access=True,  # Allow public read access
        )
        notification = s3n.SnsDestination(my_topic)
        my_bucket.add_event_notification(s3.EventType.OBJECT_CREATED, notification)

        apigateway.LambdaRestApi(
            self, f'api-id-{part}',
            rest_api_name=f'api-{part}',
            handler=my_lambda
        )
