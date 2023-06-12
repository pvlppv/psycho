from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Reply(Base):
    __tablename__ = 'reply'

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey('message.id'), index=True)
    reply_text = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.now)

    message = relationship('Message', backref='replies')
