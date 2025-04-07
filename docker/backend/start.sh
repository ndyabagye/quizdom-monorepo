#!/bin/sh

echo "Waiting for postgres at ${DATABASE_URL}..."

counter=0
until pg_isready -U postgres -h db -p 5432 || [ $counter -eq 30 ]; do
    echo "Attempt $counter: Postgres is unavailable - sleeping"
    sleep 1
    counter=$((counter+1))
done

if [ $counter -eq 30 ]; then
    echo "Failed to connect to Postgres after 30 attempts!"
    exit 1
fi

echo "PostgreSQL started successfully!"

if [ "$ENVIRONMENT" = "production" ]; then
    gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
else
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
fi