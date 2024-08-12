import uuid

from fastapi import APIRouter, UploadFile

import storage


router = APIRouter(prefix='/api/v1', tags=['MinIO Storage'])


@router.post('/objects')
def create_obj(img: UploadFile):
    img_name_prefix = str(uuid.uuid4())
    img_name = f'{img_name_prefix}_{img.filename}'
    saved_img_name = storage.save_obj(img_name, img.file)
    return saved_img_name if saved_img_name else None    # TODO: raise exception


@router.get('/objects/{name}')
def get_obj(name: str):
    # object = storage.read_obj(name)
    # return str(object)
    return storage.get_obj_link(name)


@router.put('objects/{name}')
def update_obj(name: str, img: UploadFile):
    storage.save_obj(name, img.file)
    return {'status': 'success', 'details': 'Image saved'}


@router.delete('objects/{name}')
def delete_obj(name: str):
    storage.remove_obj(name)
    return {'status': 'success', 'details': 'Image deleted'}
