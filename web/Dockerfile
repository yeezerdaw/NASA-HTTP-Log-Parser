FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y python3-distutils build-essential

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

