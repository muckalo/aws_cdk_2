"""
Database Stack Module
"""

from aws_cdk import (
    Stack,
    aws_dynamodb as ddb,
    RemovalPolicy
)
from constructs import Construct


class DatabaseStack(Stack):
    """
    Database Stack
    """

    def __init__(self, scope: Construct, _id: str, **kwargs) -> None:
        super().__init__(scope, _id, **kwargs)

        part = '2'

        self.table = ddb.Table(
            self,
            f'table-id-{part}',
            table_name=f"table-{part}",
            partition_key=ddb.Attribute(
                name="id",
                type=ddb.AttributeType.STRING
            ),
            billing_mode=ddb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY  # Removes the ddb table when the stack is deleted
        )
