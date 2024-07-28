from typing import Annotated, AsyncGenerator
from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from db import async_session_factory
from models import Meme


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    session = async_session_factory()
    try:
        yield session
    finally:
        await session.close()

async def get_meme_by_id(
    id: Annotated[int, Path],
    db: AsyncSession = Depends(get_db_session)
) -> Meme:

    meme = await db.get(Meme, id) 
    if meme is not None:
        return meme

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Meme does not exist'
    )
