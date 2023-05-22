from typing import Optional
from pydantic import BaseModel
from datetime import datetime
import pytz


class Message_Read(BaseModel):
    id: int
    lobby_name: str
    message_text: str
    created_at: datetime

    class Config:
        orm_mode=True
