"""
Network Stack Module
"""

from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct


class NetworkStack(Stack):
    """
    Network Stack
    """

    def __init__(self, scope: Construct, _id: str, **kwargs) -> None:
        super().__init__(scope, _id, **kwargs)

        part = '2'

        self.vpc = ec2.Vpc(
            self,
            f"vpc-id-{part}",
            vpc_name=f"vpc-{part}",
            max_azs=3
        )
