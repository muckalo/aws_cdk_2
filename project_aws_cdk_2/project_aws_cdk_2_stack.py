"""
AWS CDK Stack 2
"""

from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
)


class ProjectAwsCdk2Stack(Stack):
    """
    CDK Stack 2
    """

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "ProjectAwsCdk2Queue",
            visibility_timeout=Duration.seconds(300),
        )

        topic = sns.Topic(
            self, "ProjectAwsCdk2Topic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))
