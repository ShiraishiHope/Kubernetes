# Use the official Python 3.13 image as base
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Mettre à jour la liste des paquets et installer gcc/libpq-dev
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set work directory inside container
WORKDIR /app

# Copy requirements file first
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Port 8000 
EXPOSE 8000

# Command to run when container starts
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]