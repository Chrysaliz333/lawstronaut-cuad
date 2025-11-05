# Dockerfile for Lawstronaut CUAD Testing with Vertex AI
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Google Cloud and Vertex AI packages
RUN pip install --no-cache-dir \
    google-cloud-aiplatform \
    google-genai \
    google-auth \
    google-auth-oauthlib \
    google-auth-httplib2

# Copy application code
COPY *.py ./
COPY *.txt ./
COPY *.md ./

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV GOOGLE_GENAI_USE_VERTEXAI=True

# Run the application
CMD ["python", "test_gemini_vertex.py", "--questions", "all"]
