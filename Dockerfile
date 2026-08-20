FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src/ src/
COPY service/ service/

RUN pip install --no-cache-dir ".[service]"

EXPOSE 8000

ENV ROOT_PATH=""

# exec so uvicorn is PID 1 and receives SIGTERM from `docker stop` directly;
# sh -c is still needed to expand $ROOT_PATH.
CMD ["sh", "-c", "exec uvicorn service.main:app --host 0.0.0.0 --port 8000 --root-path \"$ROOT_PATH\""]
