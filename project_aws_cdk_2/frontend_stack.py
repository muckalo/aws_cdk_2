"""
Frontend Stack Module
"""

from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    RemovalPolicy
)
from constructs import Construct


class FrontendStack(Stack):
    """
    Frontend Stack
    """

    def __init__(self, scope: Construct, _id: str, **kwargs) -> None:
        super().__init__(scope, _id, **kwargs)

        part = '2'

        bucket = s3.Bucket(
            self,
            f"bucket-frontend-id-{part}",
            bucket_name=f'bucket-frontend-{part}',
            website_index_document="index.html",
            removal_policy=RemovalPolicy.DESTROY,  # Removes the bucket when the stack is deleted
            block_public_access=s3.BlockPublicAccess(
                block_public_acls=False,
                ignore_public_acls=False,
                block_public_policy=False,
                restrict_public_buckets=False
            ),  # This disables blocking
            public_read_access=True,  # Allow public read access
        )

        cloudfront.CloudFrontWebDistribution(
            self,
            f"distribution-id-{part}",
            origin_configs=[
                cloudfront.SourceConfiguration(
                    s3_origin_source=cloudfront.S3OriginConfig(s3_bucket_source=bucket),
                    behaviors=[cloudfront.Behavior(is_default_behavior=True)]
                )
            ]
        )
