FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Copy only requirements first for better caching
COPY requirements.txt ./

# Install build dependencies and requirements
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev gcc g++ libxml2-dev libxslt1-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove build-essential gcc g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Default command
CMD ["bash"]
