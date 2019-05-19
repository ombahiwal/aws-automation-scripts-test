import boto3
import pprint
#  i-03e4061d787775bcf    -   34.201.120.199

akid = 'AKIAVYQJJFT4KCOF6YPD'
sak = 'd3OXcOopaXe1ajLLJIzkSakBAHT782KVRTWUq8KT'


session = boto3.Session(
    aws_access_key_id=akid,
    aws_secret_access_key=sak
)

client = boto3.client('ec2')

# custom_filter = [{
#     "Name" : "tag:Owner",
#     "Values" : ['']
#
# }]

ec2 = boto3.resource('ec2', 'us-east-1')

running_instances = ec2.instances.filter(
    Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']
    }])

instance_ids = []
for instance in running_instances:
    if instance.tags is None:
        instance_ids.append(instance.id)

print(instance_ids)
