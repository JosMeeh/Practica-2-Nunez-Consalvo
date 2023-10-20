#!/bin/bash
set -e

# Apply database migrations using Alembic
alembic upgrade head

# Start your FastAPI application
exec uvicorn main:app --host 0.0.0.0 --port 8000
