FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Download and install Ollama CLI
RUN curl -fsSL --retry 5 --retry-delay 10 -o install.sh https://ollama.com/install.sh && \
    sh install.sh && \
    rm install.sh


# Add Ollama CLI to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose FastAPI and Streamlit ports
EXPOSE 9000
EXPOSE 8501

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


# Command to run FastAPI application
CMD ["bash", "run.sh"]

