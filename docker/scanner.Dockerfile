FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN useradd --create-home --shell /usr/sbin/nologin aisec

COPY pyproject.toml README.md ./
COPY src ./src

RUN pip install --no-cache-dir .

USER aisec

ENTRYPOINT ["aisec"]
