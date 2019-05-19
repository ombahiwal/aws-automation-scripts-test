import boto3
import pprint

akid = 'AKIAXX74YLSYAQ6XZQEA'
sak = 'zUMwIO3ExZl0BdQayLk0q70bfC2ImZx01ddoJuif'

session = boto3.Session(
    aws_access_key_id=akid,
    aws_secret_access_key=sak
)

ec2 = boto3.resource('ec2')
client = boto3.client('ec2', 'us-east-1')
#
# vpc = client.create_vpc(
#     CidrBlock='12.10.0.0/19',
#     AmazonProvidedIpv6CidrBlock=False,
#     DryRun=False,
#     InstanceTenancy='dedicated'
# )
#
# vpc_id = vpc['Vpc']['VpcId']
#
# print vpc_id
#
# #VPC-ID vpc-0c7a438522588640d
#
#
# subnet = client.create_subnet(
#     AvailabilityZone='us-east-1a',
#     CidrBlock='12.10.0.0/23',
#     VpcId=vpc_id,
#
# )
#
# # tag = ec2.Tag(subnet['Subnet']['SubnetId'],'key','value')
#
#
#
# tag = client.create_tags(
#     Resources=[
#         subnet['Subnet']['SubnetId'],
#     ],
#     Tags=[
#         {
#             'Key': 'Name',
#             'Value': 'Web1'
#         },
#     ]
# )
#
#
# print subnet['Subnet']['SubnetId']
#
# vpc_id = "vpc-003ed3b476de4b5f2"
#
# subnet = client.create_subnet(
#     AvailabilityZone='us-east-1b',
#     CidrBlock='12.10.2.0/23',
#     VpcId=vpc_id,
#
# )
#
# # tag = ec2.Tag(subnet['Subnet']['SubnetId'],'key','value')
#
#
#
# tag = client.create_tags(
#     Resources=[
#         subnet['Subnet']['SubnetId'],
#     ],
#     Tags=[
#         {
#             'Key': 'Name',
#             'Value': 'Web2'
#         },
#     ]
# )
#
# print subnet['Subnet']['SubnetId']
#
#
# subnet = client.create_subnet(
#     AvailabilityZone='us-east-1a',
#     CidrBlock='12.10.4.0/23',
#     VpcId=vpc_id,
#
# )
#
# # tag = ec2.Tag(subnet['Subnet']['SubnetId'],'key','value')
#
#
#
# tag = client.create_tags(
#     Resources=[
#         subnet['Subnet']['SubnetId'],
#     ],
#     Tags=[
#         {
#             'Key': 'Name',
#             'Value': 'App1'
#         },
#     ]
# )
#
# print subnet['Subnet']['SubnetId']
#
# subnet = client.create_subnet(
#     AvailabilityZone='us-east-1b',
#     CidrBlock='12.10.6.0/23',
#     VpcId=vpc_id,
#
# )
#
# # tag = ec2.Tag(subnet['Subnet']['SubnetId'],'key','value')
#
#
#
# tag = client.create_tags(
#     Resources=[
#         subnet['Subnet']['SubnetId'],
#     ],
#     Tags=[
#         {
#             'Key': 'Name',
#             'Value': 'App2'
#         },
#     ]
# )
#
# print subnet['Subnet']['SubnetId']
#
# subnet = client.create_subnet(
#     AvailabilityZone='us-east-1a',
#     CidrBlock='12.10.8.0/23',
#     VpcId=vpc_id,
#
# )
#
# # tag = ec2.Tag(subnet['Subnet']['SubnetId'],'key','value')
#
#
#
# tag = client.create_tags(
#     Resources=[
#         subnet['Subnet']['SubnetId'],
#     ],
#     Tags=[
#         {
#             'Key': 'Name',
#             'Value': 'DB1'
#         },
#     ]
# )
#
# print subnet['Subnet']['SubnetId']
#
#
#
# subnet = client.create_subnet(
#     AvailabilityZone='us-east-1b',
#     CidrBlock='12.10.10.0/23',
#     VpcId=vpc_id,
#
# )
#
# # tag = ec2.Tag(subnet['Subnet']['SubnetId'],'key','value')
#
#
#
# tag = client.create_tags(
#     Resources=[
#         subnet['Subnet']['SubnetId'],
#     ],
#     Tags=[
#         {
#             'Key': 'Name',
#             'Value': 'DB2'
#         },
#     ]
# )
#
# print subnet['Subnet']['SubnetId']
#
#
# #app2 - subnet-0f7bf300462450a50
# #web1 - subnet-05697238f3d3c4658
# #web2 - subnet-09f7064e308a73c1b
# #DB1 -
# #
# response = client.create_route_table(
#
#     VpcId='vpc-003ed3b476de4b5f2'
# )
# rt = response['RouteTable']['RouteTableId']
#




#
# response = client.associate_route_table(
#     RouteTableId=rt,
#     SubnetId='subnet-0990f9d299a9b4b3f'
# )
# response = client.associate_route_table(
#     RouteTableId=rt,
#     SubnetId='subnet-070b1dc0c7df675d6'
# )
# response = client.associate_route_table(
#     RouteTableId=rt,
#     SubnetId='subnet-012d2968fbd5421ab'
# )
# response = client.associate_route_table(
#     RouteTableId=rt,
#     SubnetId='subnet-0449716eba63ee4bb'
# )


# dg = client.create_security_group(
#     Description='SG for Web',
#     GroupName='WebSG',
#     VpcId='vpc-003ed3b476de4b5f2'
# )
# print dg['GroupId']
#
# dg = client.create_security_group(
#     Description='SG for App',
#     GroupName='AppWSG',
#     VpcId='vpc-003ed3b476de4b5f2'
# )
# print dg['GroupId']
#
# dg = client.create_security_group(
#     Description='SG for DB',
#     GroupName='DBSG',
#     VpcId='vpc-003ed3b476de4b5f2'
# )
# print dg['GroupId']

#
# data = client.authorize_security_group_ingress(
#         GroupId='sg-0bee8a55895707617',
#         IpPermissions=[
#             {'IpProtocol': 'tcp',
#              'FromPort': 80,
#              'ToPort': 80,
#              'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
#             {'IpProtocol': 'tcp',
#              'FromPort': 22,
#              'ToPort': 22,
#              'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
#         ])
# print('Ingress Successfully Set %s' % data)

# data = client.authorize_security_group_ingress(
#         GroupId='sg-0195a532789147d7b',
#         IpPermissions=[
#             {'IpProtocol': 'tcp',
#              'FromPort': 22,
#              'ToPort': 22,
#              'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
#         ])
# print('Ingress Successfully Set %s' % data)

# igw-0a60dc5fca658d7bf



# response = client.create_internet_gateway(
# )
#
# print response['InternetGateway']['InternetGatewayId']

# response = client.attach_internet_gateway(
#     InternetGatewayId='igw-0a60dc5fca658d7bf',
#     VpcId='vpc-003ed3b476de4b5f2'
# )
#

# response = client.create_route(
#     DestinationCidrBlock='0.0.0.0/0',
#     GatewayId='igw-0a60dc5fca658d7bf',
#     RouteTableId='rtb-019af7386e3f8e414'
# )
# print response


#
# instance_type = 't2.micro'
# volume_type = 'gp2'
# volume_size = 10
# ami_id = 'ami-6871a115'


# instances = ec2.create_instances(
#      ImageId=ami_id,
#      MinCount=1,
#      MaxCount=2,
#      InstanceType=instance_type,
#      KeyName='MyKeyPair'
# )
#
# client = boto3.client('ec2', region_name='us-east-1')
#
#
# response = client.run_instances(
#     ImageId=ami_id,
#     InstanceType=instance_type,
#     KeyName='MyKeyPair',
#     MaxCount=1,
#     MinCount=1,
#     Monitoring={
#         'Enabled': True
#     },
#     SecurityGroupId='sg-0bee8a55895707617',
#     SubnetId='subnet-0d460d17efb80e6ec'
# )
# instance_id = response['Instances'][0]['InstanceId']
# print("Instance Created with id : ", instance_id)

# vpc-003ed3b476de4b5f2
# rtb-019af7386e3f8e414
# vpc-003ed3b476de4b5f2

# subnet-0d460d17efb80e6ec

# subnet-0990f9d299a9b4b3f
# subnet-070b1dc0c7df675d6

# subnet-012d2968fbd5421ab
# subnet-0449716eba63ee4bbsg
#
# sg-0bee8a55895707617
# sg-04988d2b0f7f9e07d
# sg-0195a532789147d7b
# policy-0fbb707c49aea4822



#
# running_instances = ec2.instances.filter(
#     Filters=[{
#         'Name': 'instance-state-name',
#         'Values': ['running']
#     }])
#
# instance_ids = []
# for instance in running_instances:
#     if instance.tags is None:
#         instance_ids.append(instance.id)
#
# print(instance_ids)

#
# client = boto3.client('dlm')
# policy = {
#    "ResourceTypes": [
#       "VOLUME"
#    ],
#    "TargetTags": [
#       {
#          "Key": "test",
#          "Value": "123"
#       }
#    ],
#    "Schedules":[
#       {
#          "Name": "DailySnapshots",
#          "TagsToAdd": [
#             {
#                "Key": "type",
#                "Value": "myDailySnapshot"
#             }
#          ],
#          "CreateRule": {
#             "Interval": 24,
#             "IntervalUnit": "HOURS",
#             "Times": [
#                "00:00"
#             ]
#          },
#          "RetainRule": {
#             "Count":5
#          },
#          "CopyTags": False
#       }
#    ]
# }

#
# response = client.create_lifecycle_policy(
#     ExecutionRoleArn='arn:aws:iam::532569152688:role/342109-O',
#     Description='Test ARN',
#     State='ENABLED',
#     PolicyDetails=policy)
# print('Response', response)
# client = boto3.client('elb')
# response = client.create_load_balancer(
#     LoadBalancerName='ELB-APP',
#     Listeners=[
#         {
#             'Protocol': 'HTTP',
#             'LoadBalancerPort': 80,
#             'InstanceProtocol': 'HTTP',
#             'InstancePort': 80,
#         },
#     ],
#     AvailabilityZones=[
#         'us-east-1a',
#         'us-east-1b'
#     ],
#     Subnets=[
#         'subnet-070b1dc0c7df675d6',
#         'subnet-0990f9d299a9b4b3f'
#
#     ],
#     SecurityGroups=[
#         'sg-0bee8a55895707617'
#     ]
# )
# print response
#

response = client.create_db_cluster(
    AvailabilityZones=[
        'us-east-1a',
        'us-east-2a'
    ],
    BackupRetentionPeriod=2200,
    DatabaseName='companydb',
    DBClusterIdentifier='my-cluser-1',
    DBClusterParameterGroupName='string',
    VpcSecurityGroupIds=[
        'string',
    ],
    DBSubnetGroupName='sg-0195a532789147d7b',
    Engine='aurora',
    Port=3306,
    MasterUsername='companyrootuser',
    MasterUserPassword='omkarbahiwal',

    Tags=[
        {
            'Key': 'Name',
            'Value': 'CompanyDB'
        },
    ],
    StorageEncrypted=True|False,
    KmsKeyId='string',
    EnableIAMDatabaseAuthentication=True|False,
    BacktrackWindow=123,
    EnableCloudwatchLogsExports=[
        'string',
    ],
    EngineMode='string',
    ScalingConfiguration={
        'MinCapacity': 123,
        'MaxCapacity': 123,
        'AutoPause': True|False,
        'SecondsUntilAutoPause': 123,
        'TimeoutAction': 'string'
    },
    DeletionProtection=True|False,
    GlobalClusterIdentifier='string',
    CopyTagsToSnapshot=True|False,
    SourceRegion='string'
)
