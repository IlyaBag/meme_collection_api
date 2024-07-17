from fastapi import APIRouter, Depends, status
from sqlalchemy import Result, select
from sqlalchemy.orm import Session

from db import get_db_session
from models import Meme
import schemas


router = APIRouter(
    prefix='/api/v1',
    tags=['memes']
)


    # return [
    #     {'id': 999,
    #      'text': 'meme\'s text',
    #      'img_url': 'http://img',
    #      'created_at': '2024-07-06 22:32:37.220729'}
    # ]

@router.get('/memes', response_model=list[schemas.Meme])
def get_memes(offset: int = 0, limit: int = 5, db: Session = Depends(get_db_session)):
    stmt = select(Meme).order_by(Meme.id).offset(offset).limit(limit)
    result: Result = db.execute(stmt)
    memes = result.scalars().all()
    return memes


@router.get('/memes/{id}', response_model=schemas.Meme)
def get_meme(id: int, db: Session = Depends(get_db_session)):
    meme = db.get(Meme, id) 
    return meme


@router.post('/memes', response_model=schemas.Meme, status_code=status.HTTP_201_CREATED)
def create_meme(new_meme: schemas.MemeCreate, db: Session = Depends(get_db_session)):
    meme = Meme(**new_meme.model_dump())
    db.add(meme)
    db.commit()
    db.refresh(meme)
    return meme


@router.put('/memes/{id}', response_model=schemas.Meme)
def update_meme(id: int, new_data: schemas.MemeUpdate, db: Session = Depends(get_db_session)):
    meme = db.get(Meme, id)
    for key, val in new_data.model_dump(exclude_none=True).items():
        meme.__setattr__(key, val)
    db.flush([meme])
    db.commit()
    db.refresh(meme)
    return meme


@router.delete('/memes/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_meme(id:int, db: Session = Depends(get_db_session)):
    meme = db.get(Meme, id)
    db.delete(meme)
    db.commit()
