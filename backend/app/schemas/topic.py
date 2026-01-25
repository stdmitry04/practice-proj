from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List, Literal


class TopicSchema(BaseModel):
    id: UUID
    language_id: UUID
    name: str
    slug: str
    description: str | None
    difficulty: Literal["easy", "medium", "hard"]
    created_at: datetime

    class Config:
        from_attributes = True


class TopicListSchema(BaseModel):
    topics: List[TopicSchema]


class TopicDetailSchema(TopicSchema):
    language_name: str | None = None
