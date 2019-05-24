import boto3
import time

# Created by Omkar Bahiwal on 20th May 2019

print("---Launch Lightsail Instance---")

# Get AWS Credentials

akid = input("Enter Access Key ID : ")
sak = input("Enter Secret Access Key : ")
region = input("Enter Region : ")


AWS_ACCESS_KEY = akid
AWS_SECRET_ACCESS_KEY = sak

# initiate Client

client = boto3.client(
    'lightsail',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=region
)

# Scafolding for getting Blueprint Ids and Bundle Ids

# blueprints = client.get_blueprints()
# for bp in blueprints['blueprints']:
#     if bp['isActive']:
#         print('{} : {}'.format(bp['blueprintId'], bp['description']))

# bundles = client.get_bundles(includeInactive=False)
# for bundle in bundles['bundles']:
#     for k,v in bundle.items():
#         print('{} : {}'.format(k, v))


# Get Input Configuration of the
hostname = input("Enter Instance Name : ")
userdata = input("Enter UserData(init-script) : ")
keypair_name = input("Enter KeyPair name : ")
az = input("Enter Availability Zone : ")


# The task to perform when the newly created instance is Up and Running.
def perform_tasks():

    # Allocate a new Static IP
    print("Allocating Static IP...")
    response = client.allocate_static_ip(
        staticIpName='StaticIP' + hostname
    )
    # Attach IP to the Instance
    print("Attaching Static Ip to Instance...")
    response = client.attach_static_ip(
        staticIpName='StaticIP' + hostname,
        instanceName=hostname
    )
    # Create Snapshot of the Instance with Key "VISHAL".
    print("Creating Snapshot...")
    response = client.create_instance_snapshot(
        instanceSnapshotName=hostname + 'snapshot',
        instanceName=hostname,
        tags=[
            {
                'key': 'Vishal',
                'value': 'Snapshot'
            }
        ]
    )
    print("Instance Created.")
    # Print Configurations of the newly created instance.
    print("Response : ", create_response)


# function to check if instance is running, returns bool.
def check_instance_state():
    state_response = client.get_instance_state(
        instanceName=hostname
    )
    state = state_response["state"]["name"]
    if state == 'pending':
        time.sleep(20)
        return True
    else:
        perform_tasks()
        return False

try:

    # Create Instance Set to 5$ Instance by Default as mentioned in the task.
    print("Creating an Instance...")
    create_response = client.create_instances(
        instanceNames=[
            hostname
        ],
        availabilityZone=az,
        blueprintId='ubuntu_18_04',
        bundleId='micro_2_0',
        userData=userdata,
        keyPairName=keypair_name,
        tags=[
            {
                'key': 'Vishal',
                'value': 'MageHost'
            }]
    )
    # Check state every 30 sec to turn from Pending to Running
    print("Checking Instance State.")
    while check_instance_state():
        print(".")

except Exception as e:

    print("Some Error occured, please check the input config.")
