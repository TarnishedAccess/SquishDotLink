# squishdotlink

A URL shortener I'm building as an experiment. Might add more features later if I feel like it. A ≈week long project, including the learning portions.

## Stack
- FastAPI
- PostgreSQL (Docker)
- SQLAlchemy (async)

## Status
Work in progress. Currently have:
- Database models set up
- Base62 short-code generation
- Core logic

TBD:
- API endpoints
- Redis caching
- Click analytics
- Rate limiting

## Setup
1. Clone the repo
2. `pip install -r requirements.txt`
3. Start Postgres via Docker (see `docker-compose.yml` if present, or run manually)
4. Set up `.env` with `DATABASE_URL`
5. Run with `uvicorn app.main:app --reload`
