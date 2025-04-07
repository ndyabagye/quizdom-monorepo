FROM python:3.10-slim

WORKDIR /app

# Create and activate virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend /app

# Copy and make the startup script executable
COPY docker/backend/start.sh /app/start.sh
RUN chmod +x /app/start.sh

EXPOSE 8000

CMD ["./start.sh"]