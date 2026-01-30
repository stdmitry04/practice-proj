from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class RoadmapNode(BaseModel):
    __tablename__ = "roadmap_nodes"

    language_id = Column(UUID(as_uuid=True), ForeignKey("languages.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    position_x = Column(Integer, nullable=False, default=0)
    position_y = Column(Integer, nullable=False, default=0)
    parent_id = Column(UUID(as_uuid=True), ForeignKey("roadmap_nodes.id", ondelete="SET NULL"), nullable=True)
    order_index = Column(Integer, nullable=False, default=0)
    concept_keywords = Column(JSONB, nullable=True)
    topic = Column(String(50), nullable=True)  # For visual grouping (e.g., 'fundamentals', 'oop', 'web')
    node_type = Column(String(20), nullable=False, default='concept')  # 'concept' or 'module_test'
    module_order = Column(Integer, nullable=True)  # Determines module sequence (1-9)
    theory = Column(JSONB, nullable=True)  # Level-based theory content: {"beginner": "...", "intermediate": "...", "advanced": "...", "cheatsheet": "..."}

    language = relationship("Language", back_populates="roadmap_nodes")
    parent = relationship("RoadmapNode", remote_side="RoadmapNode.id", back_populates="children")
    children = relationship("RoadmapNode", back_populates="parent")
    problems = relationship("RoadmapProblem", back_populates="node", cascade="all, delete-orphan")

    @property
    def is_module_complete(self) -> bool:
        """Check if module test has at least 1 hard problem solved."""
        if self.node_type != 'module_test':
            return False

        hard_solved = sum(
            1 for problem in self.problems
            if problem.difficulty == 'hard' and problem.status == 'solved'
        )
        return hard_solved >= 1
