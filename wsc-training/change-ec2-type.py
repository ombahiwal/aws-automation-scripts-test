import boto3
import pprint
#  i-03e4061d787775bcf    -   34.201.120.199

# akid = 'AKIAVYQJJFT4KCOF6YPD'
# sak = 'd3OXcOopaXe1ajLLJIzkSakBAHT782KVRTWUq8KT'
akid = input("Input AKID : ")
sak = input("Input Secret KID : ")

session = boto3.Session(
    aws_access_key_id=akid,
    aws_secret_access_key=sak
)

ec2 = boto3.resource('ec2')

client = boto3.client('ec2')

# Changing Instance Type - Done
# instance_id = 'i-03e4061d787775bcf'

instance_id = input("Input Instance ID : ")
new_instance_type = input("New Instance Type : ")
# new_instance_type = 't2.micro'


def change_instance_type(inst_id, new_inst_type):
    client.stop_instances(InstanceIds=[inst_id])
    waiter = client.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=[inst_id])
    client.modify_instance_attribute(InstanceId=inst_id, Attribute='instanceType', Value=new_inst_type)
    client.start_instances(InstanceIds=[inst_id])


#this line to change single instance type

# change_instance_type(instance_id, new_instance_type)

def change_all_instances(new_inst_type):
    instances = ec2.instances.filter()
    print("Changing Instances - ")
    for instance in instances:
        print(instance.id, instance.instance_type, "=>", new_inst_type)
        change_instance_type(instance.id, new_inst_type)

change_all_instances(new_instance_type)
