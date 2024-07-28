from datetime import datetime
from pydantic import BaseModel


class MemeBase(BaseModel):
    text: str
    img_url: str


class MemeCreate(MemeBase):
    pass


class MemeUpdate(MemeBase):
    pass


class Meme(MemeBase):
    id: int
    created_at: datetime
