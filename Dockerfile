FROM python:3.9-slim

WORKDIR /flask-api

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py app.py
COPY templates templates

EXPOSE 8000

CMD flask run --host 0.0.0.0 --port 8000
