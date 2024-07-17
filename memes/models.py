from datetime import datetime
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class Meme(Base):
    __tablename__ = 'memes'

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    img_url: Mapped[str]
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True),
                                                  nullable=False,
                                                  default=datetime.utcnow)
