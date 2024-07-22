from typing import Annotated
from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from db import get_db_session
from models import Meme


def get_meme_by_id(
    id: Annotated[int, Path],
    db: Session = Depends(get_db_session)
) -> Meme:

    meme = db.get(Meme, id) 
    if meme is not None:
        return meme

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Meme does not exist'
    )

