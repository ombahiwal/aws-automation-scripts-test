# creating Snapshots and lifecycle policy.

import boto3

akid = 'AKIAVYQJJFT4KCOF6YPD'
sak = 'd3OXcOopaXe1ajLLJIzkSakBAHT782KVRTWUq8KT'
# akid = accesskey id
# sak = sec

session = boto3.Session(
    aws_access_key_id=akid,
    aws_secret_access_key=sak
)
client = boto3.client('dlm')
policy = {
   "ResourceTypes": [
      "VOLUME"
   ],
   "TargetTags": [
      {
         "Key": "test",
         "Value": "123"
      }
   ],
   "Schedules":[
      {
         "Name": "DailySnapshots",
         "TagsToAdd": [
            {
               "Key": "type",
               "Value": "myDailySnapshot"
            }
         ],
         "CreateRule": {
            "Interval": 2160,
            "IntervalUnit": "HOURS",
            "Times": [
               "00:00"
            ]
         },
         "RetainRule": {
            "Count": 5
         },
         "CopyTags": False
      }
   ]
}

try:
    response = client.create_lifecycle_policy(
        ExecutionRoleArn='arn:aws:iam::396230208760:role/test-execution-role',
        Description='Test ARN',
        State='ENABLED',
        PolicyDetails=policy)
    print('Response', response)
except:
    print("Policy Key Values Already defined")
ec2 = boto3.resource('ec2')
instance_id = 'i-00ee332c2ff01866f'
vid = 'vol-000f67bcf08866342'
snapshot = ec2.create_snapshot(VolumeId=vid, Description='description')
volume = ec2.create_volume(SnapshotId=snapshot.id, AvailabilityZone='us-east-1a')
ec2.Instance(instance_id).attach_volume(VolumeId=volume.id, Device='/dev/sdy')
snapshot.delete()
