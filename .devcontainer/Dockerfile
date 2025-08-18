FROM mcr.microsoft.com/devcontainers/python:3.12

# Install system dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
        libcairo2-dev \
        libfreetype6-dev \
        libffi-dev \
        libjpeg-dev \
        libpng-dev \
        libz-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python deps
COPY .github/workflows/requirements.txt /tmp/pip-tmp/
RUN pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp
