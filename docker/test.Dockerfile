FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

COPY pyproject.toml ./
RUN uv sync

COPY app/ ./app/
COPY tests/ ./tests/
COPY main.py ./
COPY wwwroot/ ./wwwroot/

ENV PATH="/app/.venv/bin:$PATH"

CMD ["pytest", "--cov", "--cov-report=term", "--cov-report=term-missing"]
