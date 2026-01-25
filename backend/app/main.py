from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import languages, topics, exercises

app = FastAPI(
    title="Code Practice Platform API",
    description="API for generating and running coding exercises",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://frontend:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(languages.router, prefix="/api/languages", tags=["languages"])
app.include_router(topics.router, prefix="/api/topics", tags=["topics"])
app.include_router(exercises.router, prefix="/api/exercises", tags=["exercises"])


@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
