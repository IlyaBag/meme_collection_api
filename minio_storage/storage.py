# import io
# import sys
from datetime import timedelta
from typing import BinaryIO
from minio import Minio  #, S3Error

from config import MINIO_ACCESS_KEY, MINIO_BUCKET_NAME, MINIO_SECRET_KEY


client = Minio('localhost:9000',
               access_key=MINIO_ACCESS_KEY,
               secret_key=MINIO_SECRET_KEY,
               secure=False)


found = client.bucket_exists(MINIO_BUCKET_NAME)
if not found:
    client.make_bucket(MINIO_BUCKET_NAME)


def save_obj(object_name: str, object_body: BinaryIO) -> str:
    '''Save new object in the storage.'''
    obj = client.put_object(
        bucket_name=MINIO_BUCKET_NAME,
        object_name=object_name,
        data=object_body,
        length=-1,
        part_size=5*1024*1024,
    )
    return obj.object_name

def read_obj(object_name: str) -> bytes:
    '''Get object from the storage.'''
    try:
        response = client.get_object(MINIO_BUCKET_NAME, object_name)
        # Read data from response.
        return response.data
    finally:
        response.close()
        response.release_conn()

def get_obj_link(object_name: str) -> str:
    '''Get link to download the object.'''
    link = client.get_presigned_url('GET', MINIO_BUCKET_NAME, object_name,
                                    expires=timedelta(minutes=5))
    return link

def remove_obj(object_name: str) -> None:
    '''Delete object from the storage.'''
    client.remove_object(MINIO_BUCKET_NAME, object_name)

# def main():
    # client = Minio("play.min.io",
    #     access_key="Q3AM3UQ867SPQQA43P2F",
    #     secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    # )

    # source_file = '/home/ilba/my_code/for_mad_soft/^_^tasks.md'
    # bucket_name = 'first'
    # destination_file = 'tasks.md'

    # found = client.bucket_exists(bucket_name)
    # if not found:
    #     client.make_bucket(bucket_name)
    #     print('Created bucket', bucket_name)
    # else:
    #     print('Bucket', bucket_name, 'already exists')

    # client.fput_object(bucket_name, destination_file, source_file)
    # print(
    #     source_file, 'successfully uploaded as object', destination_file,
    #     'to bucket', bucket_name
    # )
#     with open('requirements.txt', 'rb') as obj:
#         result = client.put_object(bucket_name, 'bytes_txt.txt', obj, -1, part_size=5*1024*1024)
#         f'Object {result.object_name} created.'

# if __name__ == '__main__':
#     try:
#         main()
#     except S3Error as exc:
#         print('error occurred.', exc)
