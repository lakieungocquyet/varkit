import os
from google.cloud import storage

BUCKET_NAME = "varkit"
FOLDER_PREFIX = "reference-data/hg19/variants/"

LOCAL_DIR = os.path.join(
    os.environ["HOME"],
    "varkit/reference-data/hg19/variants"
)

def download_all_objects_in_folder():
    client = storage.Client.create_anonymous_client()
    bucket = client.bucket(BUCKET_NAME)

    LOCAL_DIR.mkdir(parents=True, exist_ok=True)
    
    total = 0
    for blob in bucket.list_blobs(prefix=FOLDER_PREFIX):
        if blob.name.endswith("/"):
            continue
        relative_path = blob.name[len(FOLDER_PREFIX):]
        local_path = LOCAL_DIR / relative_path

        local_path.parent.mkdir(parents=True, exist_ok=True)

        blob.download_to_filename(local_path)
        total += 1

