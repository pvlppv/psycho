from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base


class Reply(Base):
    __tablename__ = 'reply'

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey('message.id'), index=True)
    reply_text = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.now)

    message = relationship('Message', backref='replies')
