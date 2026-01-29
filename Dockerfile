FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY . /app
WORKDIR /app

RUN uv sync

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["fastmcp", "run", "src/main.py:mcp", "--transport", "http", "--port", "8000", "--host", "0.0.0.0"]