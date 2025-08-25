
import boto3
import os
import git
import json

# --------- CONFIG ---------
GIT_REPO = "https://github.com/kanishk-malhotra/icecream_project.git"
LOCAL_DIR = "./site"
BUCKET_NAME = "my-static-site-bucket-palak123"   # must be unique globally
REGION = "ap-south-1"
INDEX_DOC = "index.html"
ERROR_DOC = "error.html"
# --------------------------

# 1. Clone Git repository
if os.path.exists(LOCAL_DIR):
    print("Repo already exists, pulling latest changes...")
    repo = git.Repo(LOCAL_DIR)
    repo.remotes.origin.pull()
else:
    print("Cloning repo...")
    git.Repo.clone_from(GIT_REPO, LOCAL_DIR)

# 2. Create S3 client
s3 = boto3.client("s3", region_name=REGION)

# 3. Create S3 bucket (if not exists)
try:
    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={"LocationConstraint": REGION},
    )
    print(f"Bucket {BUCKET_NAME} created successfully.")
except s3.exceptions.BucketAlreadyOwnedByYou:
    print(f"Bucket {BUCKET_NAME} already exists and is owned by you.")
except s3.exceptions.BucketAlreadyExists:
    print(f"Bucket {BUCKET_NAME} already exists globally. Choose another name.")

# 4. Upload all files to S3
for root, dirs, files in os.walk(LOCAL_DIR):
    for file in files:
        filepath = os.path.join(root, file)
        key = os.path.relpath(filepath, LOCAL_DIR)
        s3.upload_file(filepath, BUCKET_NAME, key, ExtraArgs={"ACL": "public-read"})
        print(f"Uploaded: {key}")

# 5. Enable static website hosting
s3.put_bucket_website(
    Bucket=BUCKET_NAME,
    WebsiteConfiguration={
        "IndexDocument": {"Suffix": INDEX_DOC},
        "ErrorDocument": {"Key": ERROR_DOC},
    },
)

# 6. Set bucket policy for public access
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{BUCKET_NAME}/*",
        }
    ],
}

s3.put_bucket_policy(Bucket=BUCKET_NAME, Policy=json.dumps(policy))

print("\n✅ Static website hosting enabled!")
print(f"👉 Website URL: http://{BUCKET_NAME}.s3-website.{REGION}.amazonaws.com")
