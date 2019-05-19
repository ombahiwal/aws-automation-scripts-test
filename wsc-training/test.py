import boto3
import json
akid = 'AKIAVYQJJFT4KCOF6YPD'
sak = 'd3OXcOopaXe1ajLLJIzkSakBAHT782KVRTWUq8KT'

session = boto3.Session(
    aws_access_key_id=akid,
    aws_secret_access_key=sak
)

msg = "Breach Detected in RDS, someone create a DB with name "
# msg = msg + " ID :" + instance['DBInstanceIdentifier'] + " PA : " + instance['PubliclyAccessible']
message = {"RDS-Breach": msg}
required_sg_ids = ["sg-04e05c050b9259ac2", "sg-03c17fe8df0ea35fd"]

client = boto3.client('rds', 'ap-south-1')
sns = boto3.client('sns', 'ap-south-1')
arn = "arn:aws:sns:ap-south-1:396230208760:test"

response2 = sns.publish(
                    TargetArn=arn,
                    Message=json.dumps({'default': json.dumps(message)}),
                    MessageStructure='json'
                )