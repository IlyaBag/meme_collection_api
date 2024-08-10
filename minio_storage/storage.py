from typing import BinaryIO
from minio import Minio

from config import MINIO_ACCESS_KEY, MINIO_BUCKET_NAME, MINIO_SECRET_KEY


client = Minio('localhost:9000',
               access_key=MINIO_ACCESS_KEY,
               secret_key=MINIO_SECRET_KEY,
               secure=False)


found = client.bucket_exists(MINIO_BUCKET_NAME)
if not found:
    client.make_bucket(MINIO_BUCKET_NAME)


def save_obj(object_name: str, object_body: BinaryIO):
    '''Save new object in the storage.'''
    ...

def read_obj(id):
    '''Get object from the storage by ID.'''
    ...

def rewrite_obj(id):
    '''Update (replace) object in the storage.'''
    ...

def remove_obj(id):
    '''Delete object from the storage.'''
    ...
