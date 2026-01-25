from sqlalchemy import Column, String, Text, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Exercise(BaseModel):
    __tablename__ = "exercises"

    topic_id = Column(UUID(as_uuid=True), ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    template_code = Column(Text, nullable=False)
    solution_code = Column(Text, nullable=False)
    test_cases = Column(JSON, nullable=False)
    hints = Column(JSON, nullable=True)

    topic = relationship("Topic", back_populates="exercises")
