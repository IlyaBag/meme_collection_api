from datetime import datetime
from pydantic import BaseModel


class Meme(BaseModel):
    id: int
    text: str
    img_url: str
    created_at: datetime
