from fastapi import APIRouter, Depends, status
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from db import get_db_session
from api_v1.dependencies import get_meme_by_id
from models import Meme
import api_v1.schemas as schemas


router = APIRouter(
    prefix='/api/v1',
    tags=['memes']
)


@router.get('/memes', response_model=list[schemas.Meme])
async def get_memes(
    offset: int = 0,
    limit: int = 5,
    db: AsyncSession = Depends(get_db_session)
):
    stmt = select(Meme).order_by(Meme.id).offset(offset).limit(limit)
    result: Result = await db.execute(stmt)
    memes = result.scalars().all()
    return memes


@router.get('/memes/{id}', response_model=schemas.Meme)
async def get_meme(meme: Meme = Depends(get_meme_by_id)):
    return meme


@router.post('/memes',
             response_model=schemas.Meme,
             status_code=status.HTTP_201_CREATED)
async def create_meme(
    new_meme: schemas.MemeCreate,
    db: AsyncSession = Depends(get_db_session)
):
    meme = Meme(**new_meme.model_dump())
    db.add(meme)
    await db.commit()
    await db.refresh(meme)
    return meme


@router.put('/memes/{id}', response_model=schemas.Meme)
async def update_meme(
    new_data: schemas.MemeUpdate,
    db: AsyncSession = Depends(get_db_session),
    meme: Meme = Depends(get_meme_by_id)
):
    for key, val in new_data.model_dump(exclude_none=True).items():
        meme.__setattr__(key, val)
    await db.commit()
    return meme


@router.delete('/memes/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_meme(
    db: AsyncSession = Depends(get_db_session),
    meme: Meme = Depends(get_meme_by_id)
) -> None:
    await db.delete(meme)
    await db.commit()
