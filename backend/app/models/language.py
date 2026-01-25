from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Language(BaseModel):
    __tablename__ = "languages"

    name = Column(String(50), nullable=False)
    slug = Column(String(50), nullable=False, unique=True)
    icon = Column(String(50), nullable=True)

    topics = relationship("Topic", back_populates="language", cascade="all, delete-orphan")
