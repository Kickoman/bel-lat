FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src/ src/
COPY service/ service/

RUN pip install --no-cache-dir ".[service]"

EXPOSE 8000

ENV ROOT_PATH=""
# Unbuffered stdout: without it log lines sit in the buffer and reach the
# collector in delayed bursts instead of as they happen.
ENV PYTHONUNBUFFERED=1
ENV SERVICE_NAME="bel-lat"

# exec so uvicorn is PID 1 and receives SIGTERM from `docker stop` directly;
# sh -c is still needed to expand $ROOT_PATH.
# --no-proxy-headers: uvicorn otherwise rewrites request.client from the
# forwarded headers when the peer is trusted, which erases the one address
# that is always true. The app records both itself, deliberately.
CMD ["sh", "-c", "exec uvicorn service.main:app --host 0.0.0.0 --port 8000 --no-proxy-headers --root-path \"$ROOT_PATH\""]
