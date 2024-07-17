from datetime import datetime
from pydantic import BaseModel


class MemeBase(BaseModel):
    text: str
    img_url: str


class MemeCreate(MemeBase):
    pass


class MemeUpdate(MemeBase):
    text: str | None = None
    img_url: str | None = None


class Meme(MemeBase):
    id: int
    created_at: datetime
