from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Topic(BaseModel):
    __tablename__ = "topics"

    language_id = Column(UUID(as_uuid=True), ForeignKey("languages.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    difficulty = Column(String(20), nullable=False)  # 'easy', 'medium', 'hard'

    language = relationship("Language", back_populates="topics")
    exercises = relationship("Exercise", back_populates="topic", cascade="all, delete-orphan")
