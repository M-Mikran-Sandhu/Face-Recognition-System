# Use Python 3.11 slim base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN apt-get update \
    && apt-get install -y --no-install-recommends libgl1 libglib2.0-0 libsm6 libxrender1 libxext6 \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY src ./src

# Expose Flask port
EXPOSE 5000

# Environment variables for Flask
ENV FLASK_APP=src/main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Launch the application
CMD ["python", "src/main.py"]