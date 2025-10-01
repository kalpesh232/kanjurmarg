# Use an official slim Python image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install small build deps (needed if pip compiles anything)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
 && rm -rf /var/lib/apt/lists/*

# Copy dependency file first (cache pip layer)
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy app code
COPY . .

# Create non-root user for safety
RUN useradd -m appuser
USER appuser

EXPOSE 5000

# Use gunicorn for production; app:app assumes your Flask app object is named `app` in app.py
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
