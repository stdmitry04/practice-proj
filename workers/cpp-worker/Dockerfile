FROM python:3.11-slim

WORKDIR /app

# Install g++ compiler
RUN apt-get update && apt-get install -y \
    g++ \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

# Create non-root user for security
RUN useradd -m -s /bin/bash runner

EXPOSE 5000

CMD ["python", "main.py"]
