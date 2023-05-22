from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    lobby_name = Column(String, ForeignKey('lobby.name'), index=True)
    message_text = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.now)

    message = relationship('Lobby', backref='messages')

class Lobby(Base):
    __tablename__ = 'lobby'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

