# Use official Python image
FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy project files
COPY app/ ./app/
COPY tests/ ./tests/

# Set PYTHONPATH
ENV PYTHONPATH=/app

# Run auto_test.py by default
CMD ["python", "auto_test.py"]
