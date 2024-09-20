"""
TEST
"""

import aws_cdk as core
from aws_cdk import assertions
from project_aws_cdk_2.project_aws_cdk_2_stack import ProjectAwsCdk2Stack


def test_sqs_queue_created():
    """
    Test SQS

    :return:
    """

    app = core.App()
    stack = ProjectAwsCdk2Stack(app, "project-aws-cdk-2")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    """
    Test SNS

    :return:
    """

    app = core.App()
    stack = ProjectAwsCdk2Stack(app, "project-aws-cdk-2")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
