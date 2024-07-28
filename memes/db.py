from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from config import DB_HOST, DB_NAME, DB_PORT, DB_ECHO, DB_PASS, DB_USER


engine = create_async_engine(
    f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
    echo=DB_ECHO,
)

async_session_factory = async_sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False,
)
