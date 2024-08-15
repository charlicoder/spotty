FROM --platform=linux/amd64 python:3.12-slim AS build

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    libcurl4-openssl-dev

# Install Python dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the Django app code into the container
COPY . .

COPY entrypoint.sh /app/

# Grant execute permissions to the entrypoint script
RUN chmod +x /app/entrypoint.sh

# Expose the port that Gunicorn will listen on
EXPOSE 8000

# Set the entrypoint script as the container entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
