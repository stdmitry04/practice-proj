from sqlalchemy import Column, String, Text, Enum, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import enum

from app.models.base import BaseModel


class DifficultyEnum(str, enum.Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"


class StatusEnum(str, enum.Enum):
    unsolved = "unsolved"
    attempted = "attempted"
    solved = "solved"


class RoadmapProblem(BaseModel):
    __tablename__ = "roadmap_problems"

    node_id = Column(UUID(as_uuid=True), ForeignKey("roadmap_nodes.id", ondelete="CASCADE"), nullable=False)
    difficulty = Column(Enum(DifficultyEnum), nullable=False, default=DifficultyEnum.easy)
    status = Column(Enum(StatusEnum), nullable=False, default=StatusEnum.unsolved)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    template_code = Column(Text, nullable=False)
    solution_code = Column(Text, nullable=False)
    test_cases = Column(JSON, nullable=False)
    hints = Column(JSON, nullable=True)
    description_hash = Column(String(64), nullable=False, unique=True)
    condensed_description = Column(Text, nullable=False)

    node = relationship("RoadmapNode", back_populates="problems")
