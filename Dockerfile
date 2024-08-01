FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git gcc libpq-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt --verbose

COPY . .



CMD ["python", "PruebaVet.py"]
