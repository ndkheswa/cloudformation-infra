from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    core,
)

from aws_cdk.core import Tag

class AcaInfraStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc.from_lookup(
            self, 'VPC',
            vpc_id = 'vpc-0828450a799156d44',
            subnet_group_name_tag = 'app'
        )
        Tag.add(self, "TeamCode", "aca")

        cluster = ecs.Cluster(
            self, 'aca-dev-cluster',
            vpc=vpc
        )

        ecs_patterns.ApplicationLoadBalancedFargateService(self, "aca-dev-svc",
            cluster=cluster,            # Required
            cpu=512,                    # Default is 256
            desired_count=2,            # Default is 1
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
            image=ecs.ContainerImage.from_registry("167172578651.dkr.ecr.eu-west-1.amazonaws.com/aca-web:0.2.8")),
            memory_limit_mib=2048      # Default is 512
        )