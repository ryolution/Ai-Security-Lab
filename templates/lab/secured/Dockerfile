FROM python:3.12-slim

WORKDIR /app
COPY app.py .

CMD ["python", "-c", "from app import handle_request; print(handle_request('demo', 'synthetic context'))"]
