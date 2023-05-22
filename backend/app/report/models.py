from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base


class Report(Base):
    __tablename__ = 'report'

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey('message.id'), index=True)
    report_text = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.now)

    message = relationship('Message', backref='reports')
