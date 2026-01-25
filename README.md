# Code Practice Platform

A web service for practicing coding exercises across React, JavaScript, Python, and C++. Users select a language, pick a topic, and AI generates tasks with solutions.

## Features

- **Multi-language Support:** React, JavaScript, Python, and C++
- **AI-Generated Exercises:** GPT-4 generates unique practice tasks with test cases
- **Split-Panel UI:** Task description on left, code editor on right
- **Real-time Code Execution:** Sandboxed workers execute code safely
- **Test-Based Verification:** Automatic validation against test cases

## Tech Stack

### Backend
- FastAPI (Python 3.11)
- PostgreSQL 16
- SQLAlchemy 2.x + Alembic
- OpenAI GPT-4

### Frontend
- Next.js 15 (App Router)
- React 19 + TypeScript
- Tailwind CSS
- Monaco Editor
- Zustand

### Infrastructure
- Docker Compose
- Persistent language workers

## Quick Start

### Prerequisites
- Docker & Docker Compose
- OpenAI API key

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd practice-proj
```

2. Create environment file:
```bash
cp .env.example .env
```

3. Add your OpenAI API key to `.env`:
```
OPENAI_API_KEY=sk-your-key-here
```

4. Start all services:
```bash
docker-compose up --build
```

5. Access the application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Development

### Running Backend Only
```bash
docker-compose up db backend
```

### Running Migrations
```bash
docker-compose exec backend alembic upgrade head
```

### Seeding Data
```bash
docker-compose exec backend python seed_data.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/languages` | List all languages |
| GET | `/api/languages/{id}/topics` | List topics for a language |
| GET | `/api/topics/{id}` | Get topic details |
| POST | `/api/exercises/generate` | Generate new exercise |
| GET | `/api/exercises/{id}` | Get existing exercise |
| POST | `/api/exercises/{id}/submit` | Submit code for verification |

## Project Structure

```
practice-proj/
├── backend/           # FastAPI backend
│   ├── app/
│   │   ├── models/    # SQLAlchemy models
│   │   ├── schemas/   # Pydantic schemas
│   │   ├── routers/   # API routes
│   │   └── services/  # Business logic
│   └── alembic/       # Database migrations
├── workers/           # Code execution workers
│   ├── python-worker/
│   ├── javascript-worker/
│   ├── cpp-worker/
│   └── react-worker/
├── frontend/          # Next.js frontend
│   ├── app/           # App router pages
│   ├── components/    # React components
│   ├── lib/           # Utilities
│   └── stores/        # Zustand stores
└── docker-compose.yml
```

## Security

- Code execution in isolated Docker containers
- Subprocess timeouts and memory limits
- No external network access for workers
- Input sanitization

## License

MIT
