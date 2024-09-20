#!/usr/bin/env python3

"""
App Module
"""

import aws_cdk as cdk

# from project_aws_cdk_2.project_aws_cdk_2_stack import ProjectAwsCdk2Stack
from project_aws_cdk_2.network_stack import NetworkStack
from project_aws_cdk_2.database_stack import DatabaseStack
from project_aws_cdk_2.backend_stack import BackendStack
from project_aws_cdk_2.frontend_stack import FrontendStack


app = cdk.App()

network_stack = NetworkStack(app, "NetworkStack")

database_stack = DatabaseStack(app, "DatabaseStack")
database_stack.add_dependency(network_stack)

backend_stack = BackendStack(app, "BackendStack", vpc=network_stack.vpc, table=database_stack.table)
backend_stack.add_dependency(database_stack)

frontend_stack = FrontendStack(app, "FrontendStack")
frontend_stack.add_dependency(backend_stack)

app.synth()
