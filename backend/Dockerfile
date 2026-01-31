FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run migrations, seed data, and start server
CMD ["sh", "-c", "alembic upgrade head && python seed_data.py && python seed_roadmap.py && python seed_roadmap_leveled.py && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]
