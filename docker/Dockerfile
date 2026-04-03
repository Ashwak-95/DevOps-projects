FROM python:3.11-slim

WORKDIR /app

# Install dependencies (cached layer)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

EXPOSE 5000

CMD ["python3", "app.py"]