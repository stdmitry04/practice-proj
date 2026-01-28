from sqlalchemy import Column, String, Text, Integer, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
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
    concept_keywords = Column(JSON, nullable=True)

    language = relationship("Language", back_populates="roadmap_nodes")
    parent = relationship("RoadmapNode", remote_side="RoadmapNode.id", back_populates="children")
    children = relationship("RoadmapNode", back_populates="parent")
    problems = relationship("RoadmapProblem", back_populates="node", cascade="all, delete-orphan")
