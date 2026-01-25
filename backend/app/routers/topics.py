from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.models.topic import Topic
from app.schemas.topic import TopicSchema, TopicDetailSchema

router = APIRouter()


@router.get("/{topic_id}", response_model=TopicDetailSchema)
async def get_topic(topic_id: UUID, db: Session = Depends(get_db)):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    return TopicDetailSchema(
        id=topic.id,
        language_id=topic.language_id,
        name=topic.name,
        slug=topic.slug,
        description=topic.description,
        difficulty=topic.difficulty,
        created_at=topic.created_at,
        language_name=topic.language.name if topic.language else None
    )
