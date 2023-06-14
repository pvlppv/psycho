from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True)
    lobby_name = Column(String, ForeignKey("lobby.name"), index=True)
    message_text = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.now)

    message = relationship("Lobby", backref="messages")


class Lobby(Base):
    __tablename__ = "lobby"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
