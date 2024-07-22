from fastapi import APIRouter, Depends, status
from sqlalchemy import Result, select
from sqlalchemy.orm import Session

from db import get_db_session
from api_v1.dependencies import get_meme_by_id
from models import Meme
import schemas


router = APIRouter(
    prefix='/api/v1',
    tags=['memes']
)


@router.get('/memes', response_model=list[schemas.Meme])
def get_memes(
    offset: int = 0,
    limit: int = 5,
    db: Session = Depends(get_db_session)
):
    stmt = select(Meme).order_by(Meme.id).offset(offset).limit(limit)
    result: Result = db.execute(stmt)
    memes = result.scalars().all()
    return memes


@router.get('/memes/{id}', response_model=schemas.Meme)
def get_meme(meme: Meme = Depends(get_meme_by_id)):
    return meme


@router.post('/memes',
             response_model=schemas.Meme,
             status_code=status.HTTP_201_CREATED)
def create_meme(
    new_meme: schemas.MemeCreate,
    db: Session = Depends(get_db_session)
):
    meme = Meme(**new_meme.model_dump())
    db.add(meme)
    db.commit()
    db.refresh(meme)
    return meme


@router.put('/memes/{id}', response_model=schemas.Meme)
def update_meme(
    new_data: schemas.MemeUpdate,
    db: Session = Depends(get_db_session),
    meme: Meme = Depends(get_meme_by_id)
):
    for key, val in new_data.model_dump(exclude_none=True).items():
        meme.__setattr__(key, val)
    db.commit()
    return meme


@router.delete('/memes/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_meme(
    db: Session = Depends(get_db_session),
    meme: Meme = Depends(get_meme_by_id)
) -> None:

    db.delete(meme)
    db.commit()
