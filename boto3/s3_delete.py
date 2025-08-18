import boto3

def delete_all_buckets():
    s3 = boto3.resource('s3')
    
    for bucket in s3.buckets.all():
        print(f"🗑 Deleting bucket: {bucket.name}")
        
        # Delete all objects
        bucket.objects.all().delete()
        
        # Check and delete all versions if versioning is enabled
        bucket_versioning = s3.BucketVersioning(bucket.name)
        if bucket_versioning.status == 'Enabled':
            bucket.object_versions.all().delete()
        
        # Delete bucket itself
        bucket.delete()
        print(f"✅ Bucket '{bucket.name}' deleted.")

delete_all_buckets()

