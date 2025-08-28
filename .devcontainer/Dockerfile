FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libcairo2-dev \
    libfreetype6-dev \
    libffi-dev \
    libjpeg-dev \
    libpng-dev \
    libz-dev \
    && rm -rf /var/lib/apt/lists/*

# Ensure pip is available and up to date
RUN python -m pip install --upgrade pip setuptools wheel