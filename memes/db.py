from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import DB_HOST, DB_NAME, DB_PORT, POSTGRES_PASSWORD, POSTGRES_USER


DB_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DB_URL, echo=True)

SessionLocal = sessionmaker(engine)

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass
