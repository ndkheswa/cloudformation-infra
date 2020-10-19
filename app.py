#!/usr/bin/env python3

from aws_cdk import core

from aca_infra.aca_infra_stack import AcaInfraStack


app = core.App()
AcaInfraStack(app, "aca-infra")

app.synth()
