from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@db:5432/practice_db"
    openai_api_key: str = ""

    python_worker_url: str = "http://python-worker:5000"
    javascript_worker_url: str = "http://javascript-worker:5000"
    cpp_worker_url: str = "http://cpp-worker:5000"
    react_worker_url: str = "http://react-worker:5000"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
