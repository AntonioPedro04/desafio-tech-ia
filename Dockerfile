
FROM python:3.9-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app
COPY data/ ./data
COPY notebooks/ ./notebooks

EXPOSE 8000

CMD ["uvicorn", "app.api.endpoints:app", "--host", "0.0.0.0", "--port", "8000"]