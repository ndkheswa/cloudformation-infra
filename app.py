#!/usr/bin/env python3

from aws_cdk import core

from aca_infra.aca_infra_stack import AcaInfraStack


app = core.App()
AcaInfraStack(app, "aca-ec2", env={'region': 'eu-west-1', 'account': '167172578651'})

app.synth()
