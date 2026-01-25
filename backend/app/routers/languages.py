from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from app.database import get_db
from app.models.language import Language
from app.models.topic import Topic
from app.schemas.language import LanguageSchema
from app.schemas.topic import TopicSchema

router = APIRouter()


@router.get("", response_model=List[LanguageSchema])
async def get_languages(db: Session = Depends(get_db)):
    languages = db.query(Language).order_by(Language.name).all()
    return languages


@router.get("/{language_id}", response_model=LanguageSchema)
async def get_language(language_id: UUID, db: Session = Depends(get_db)):
    language = db.query(Language).filter(Language.id == language_id).first()
    if not language:
        raise HTTPException(status_code=404, detail="Language not found")
    return language


@router.get("/{language_id}/topics", response_model=List[TopicSchema])
async def get_language_topics(language_id: UUID, db: Session = Depends(get_db)):
    language = db.query(Language).filter(Language.id == language_id).first()
    if not language:
        raise HTTPException(status_code=404, detail="Language not found")

    topics = db.query(Topic).filter(Topic.language_id == language_id).order_by(Topic.name).all()
    return topics
