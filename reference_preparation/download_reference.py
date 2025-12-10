import os
from google.cloud import storage

BUCKET_NAME = "varkit"
FOLDER_PREFIX = "reference-data/hg19/variants/"

LOCAL_DIR = os.path.join(
    os.environ["HOME"],
    "varkit/reference-data/hg19/variants"
)
os.makedirs(LOCAL_DIR, exist_ok=True)
def download_all_objects_in_folder():
    client = storage.Client.create_anonymous_client()
    bucket = client.bucket(BUCKET_NAME)
    
    total = 0
    for blob in bucket.list_blobs(prefix=FOLDER_PREFIX):
        if blob.name.endswith("/"):
            continue
        relative_path = blob.name[len(FOLDER_PREFIX):]
        local_path = os.path.join(LOCAL_DIR, relative_path)

        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        blob.download_to_filename(local_path)
        total += 1
download_all_objects_in_folder()
