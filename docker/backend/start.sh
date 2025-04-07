#!/bin/sh

echo "Waiting for postgres..."

until pg_isready -U postgres -h db -p 5432; do
    echo "Postgres is unavailable - sleeping"
    sleep 1
done

echo "PostgreSQL started"

if [ "$ENVIRONMENT" = "production" ]; then
    gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
else
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
fi