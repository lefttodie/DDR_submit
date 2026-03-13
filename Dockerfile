FROM python:3.11-slim

WORKDIR /app

# install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# copy requirements first
COPY requirements.txt .

# install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# create directories
RUN mkdir -p uploads reports

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]