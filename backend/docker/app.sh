#!/bin/bash
alembic upgrade head
cd app
cat .env-non-dev | gunicorn app:app --workers ${BACKEND_WORKERS} --worker-class uvicorn.workers.UvicornWorker --bind=${BACKEND_HOST}:${BACKEND_PORT} --log-level ${BACKEND_LOG_LEVEL}