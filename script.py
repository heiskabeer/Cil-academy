import os
import boto3
from datetime import datetime

s3 = boto3.resource('s3')

bucket_name = 'c6m3-bucket-test'
ec2_url = '/home/ssm-user/mys3backup/'


def backup_bucket():
    os.makedirs(ec2_url, exist_ok=True)

    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.all():
        key = obj.key
        local_path = os.path.join(ec2_url, key)
        bucket.download_file(key, local_path) 
    
    print(f"Backup completed at {datetime.now()}")


if __name__ == "__main__":
    backup_bucket()

