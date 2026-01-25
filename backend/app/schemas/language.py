from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List


class LanguageSchema(BaseModel):
    id: UUID
    name: str
    slug: str
    icon: str | None
    created_at: datetime

    class Config:
        from_attributes = True


class LanguageListSchema(BaseModel):
    languages: List[LanguageSchema]
