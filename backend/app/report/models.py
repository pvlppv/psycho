from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Report(Base):
    __tablename__ = "report"

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey("message.id"), index=True)
    report_text = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.now)

    message = relationship("Message", backref="reports")
