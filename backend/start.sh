#!/bin/bash
cp -rf .env-non-dev app/.env
alembic upgrade head
source .env-non-dev
cd app
gunicorn app:app --workers $BACKEND_WORKERS --worker-class uvicorn.workers.UvicornWorker --bind=$BACKEND_HOST:$BACKEND_PORT --log-level $BACKEND_LOG_LEVEL