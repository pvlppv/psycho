from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, Integer, String

from db import Base


class EarlyAccess(Base):
    __tablename__ = 'early-access'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(length=256), nullable=False)
    type = Column(String, nullable=False, default="main")
    status = Column(String, nullable=False, default="waiting")
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.now)
