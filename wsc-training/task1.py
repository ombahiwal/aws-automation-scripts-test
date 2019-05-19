
#creating Ec2 instance with a keypair, returnign instance id

import boto3
import pprint

akid = 'AKIAVYQJJFT4KCOF6YPD'
sak = 'd3OXcOopaXe1ajLLJIzkSakBAHT782KVRTWUq8KT'

session = boto3.Session(
    aws_access_key_id=akid,
    aws_secret_access_key=sak
)

ec2 = boto3.resource('ec2')
# creating key, generate new key if not present

try:
    keyname = 'ec2-key-pair'
    # keyname = input("Enter keypair name to associate : ")
    outfile = open('ec2-key-pair.pem', 'w')
    key_pair = ec2.create_key_pair(KeyName=keyname)
    KeyPairOut = str(key_pair.key_material)
    print(KeyPairOut)
    outfile.write(KeyPairOut)
except:
    print('key pair already exists as ec2-key-pair.pem')
finally:
    outfile.close()

# get Instance details

# ami_id = input("Enter AMI Id : ")
# instance_type = input("Enter instance type : ")
# volume_type = input("Enter Volume Type : ")
# volume_size = input("Enter Volume Size : ")
instance_type = 't2.nano'
volume_type = 'gp2'
volume_size = 8
ami_id = 'ami-0a313d6098716f372'

# instances = ec2.create_instances(
#      ImageId=ami_id,
#      MinCount=1,
#      MaxCount=2,
#      InstanceType=instance_type,
#      KeyName=key_pair
# )

client = boto3.client('ec2', region_name='us-east-1')
response = client.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {

                'DeleteOnTermination': True,
                'VolumeSize': 8,
                'VolumeType': 'gp2'
            },
        },
    ],
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_pair,
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': False
    },
)
instance_id = response['Instances'][0]['InstanceId']
print("Instance Created with id : ", instance_id)




# from operator import itemgetter
#
# client = boto3.client('ec2')
# response = client.describe_images(
#     Filters=[
#         {
#             'Name': 'description',
#             'Values': [
#                 'Amazon Machine Linux*',
#             ]
#         },
#     ],
#     Owners=[
#         'amazon'
#     ]
# )
# import boto3
#
# client = boto3.client('ec2', region_name='us-west-2')
#
# response = client.run_instances(
#     BlockDeviceMappings=[
#         {
#             'DeviceName': '/dev/xvda',
#             'Ebs': {
#
#                 'DeleteOnTermination': True,
#                 'VolumeSize': 8,
#                 'VolumeType': 'gp2'
#             },
#         },
#     ],
#     ImageId='ami-6cd6f714',
#     InstanceType='t3.micro',
#     MaxCount=1,
#     MinCount=1,
#     Monitoring={
#         'Enabled': False
#     },
#     SecurityGroupIds=[
#         'sg-1f39854x',
#     ],
# )
# Sort on Creation date Desc
# image_details = sorted(response['Images'],key=itemgetter('CreationDate'),reverse=True)
# ami_id = image_details[0]['ImageId']
# print ami_id

