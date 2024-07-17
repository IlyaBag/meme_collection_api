from fastapi import APIRouter, Depends
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

