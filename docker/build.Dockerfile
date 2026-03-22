FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml ./
RUN uv sync --no-dev

COPY app/ ./app/
COPY main.py ./
COPY wwwroot/ ./wwwroot/

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uvicorn", "main:asgi_app", "--host", "0.0.0.0", "--port", "8000"]
