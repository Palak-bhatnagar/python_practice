import boto3

def count_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    
    bucket_count = len(response['Buckets'])
    print(f"📦 Total S3 Buckets: {bucket_count}")
    
    # Optional: Print bucket names
    for bucket in response['Buckets']:
        print(f"- {bucket['Name']}")
    
    return bucket_count

# Example
count_s3_buckets()

