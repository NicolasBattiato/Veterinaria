FROM python:3.12-slim

WORKDIR /app
RUN apt-get update && apt-get install -y git
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5432

CMD ["python", "PruebaVet.py"]