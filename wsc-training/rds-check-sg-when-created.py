
import boto3
import pprint
import json

akid = 'AKIAVYQJJFT4KCOF6YPD'
sak = 'd3OXcOopaXe1ajLLJIzkSakBAHT782KVRTWUq8KT'

session = boto3.Session(
    aws_access_key_id=akid,
    aws_secret_access_key=sak
)

required_sg_ids = ["sg-04e05c050b9259ac2", "sg-03c17fe8df0ea35fd"]

client = boto3.client('rds', 'ap-south-1')
sns = boto3.client('sns', 'ap-south-1')
arn = "arn:aws:sns:ap-south-1:396230208760:test"
dbname = []
response = client.describe_db_instances()
# print response

# print response['DBInstances'][0]['VpcSecurityGroups'][0]['VpcSecurityGroupId']
# print response['DBInstances'][0]['DBSecurityGroups']
# print response['DBInstances'][0]['DBInstanceStatus']
# print response['DBInstances'][0]['DBName']
# print response['DBInstances'][0]['PubliclyAccessible']
#


breach = []
print response
try:
    for i in range(0, len(response['DBInstances'])):
        instance = response['DBInstances'][i]
        for j in range(0, len(instance['VpcSecurityGroups'])):
            if not (instance['VpcSecurityGroups'][j]['VpcSecurityGroupId'] in required_sg_ids) or instance['PubliclyAccessible']:
                dbname.append(instance['DBName'])
                breach.append(instance['PubliclyAccessible'])
                response1 = client.delete_db_instance(
                    DBInstanceIdentifier=instance['DBInstanceIdentifier'],
                    SkipFinalSnapshot=True,
                    DeleteAutomatedBackups=True
                )
                msg = "Breach Detected in RDS, someone create a DB with name " + instance['DBName']
                msg = msg + " ID :"+ instance['DBInstanceIdentifier'] +" PA : " + str(instance['PubliclyAccessible'])
                message = {"RDS-Breach": msg}

                response2 = sns.publish(
                    TargetArn=arn,
                    Message=json.dumps({'default': json.dumps(message)}),
                    MessageStructure='json'
                )

except:
    print "Instances Safe | or being already deleted"
