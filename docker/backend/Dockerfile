FROM python:3:10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000

# Development environment (auto-reload)
CMD if ["$ENVIRONMENT" == "production"]; then \
	gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000; \
	else \
	uvicorn main:app --reload --host 0.0.0.0 --port 8000; \
	fi