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

# instance_id = 'i-03504d72d24d8ef8b'
# sec_grp_id = 'sg-0ddaa2063d0/eade0c'


instance_id = input("Input Instance Id : ")
sec_grp_id = input("Security Group Id to Change to : ")

def change_all_sec_group(sg_id):
    instances = ec2.instances.filter()
    for instance in instances:
        print(instance.id, instance.instance_type)
        all_sg_ids = [sg['GroupId'] for sg in
                      instance.security_groups]
        if sg_id in all_sg_ids:
            all_sg_ids.remove(sg_id)
            instance.modify_attribute(Groups=all_sg_ids)


def change_sec_grp(sg_id, inst_id):

    instances = ec2.instances.filter(InstanceIds=[inst_id])
    for instance in instances:
        print("SG for ", instance.id, "Changed to", sg_id)
        instance.modify_attribute(Groups=[sg_id])

change_sec_grp(sec_grp_id, instance_id)