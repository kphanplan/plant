from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.models import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())