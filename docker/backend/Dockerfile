# Builder stage
FROM python:3.10-slim AS builder

# Install postgres client in builder (will be discarded)
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY backend/requirements.txt .
RUN python3 -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt && \
	/venv/bin/pip install --no-cache-dir uvicorn gunicorn

# Runtime stage
FROM python:3.10-slim

# Install postgres client in runtime image
RUN apt-get update && \
	apt-get install -y postgresql-client && \
	rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"
COPY backend /app
COPY docker/backend/start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh

EXPOSE 8000
CMD ["/usr/local/bin/start.sh"]