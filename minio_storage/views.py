from fastapi import APIRouter



router = APIRouter(prefix='/api/v1', tags=['MinIO Storage'])


@router.post('/objects')
def create_obj():
    ...


@router.get('/objects/{id}')
def get_obj(id):
    ...


@router.put('objects/{id}')
def update_obj(id):
    ...


@router.delete('objects/{id}')
def delete_obj(id):
    ...
