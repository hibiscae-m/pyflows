FROM python:3.10.21-alpine3.24s

WORKDIR /app

COPY main.py requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

ARG FASTAPI_PORT=8000
ENV FASTAPI_PORT=${FASTAPI_PORT}
EXPOSE ${FASTAPI_PORT}

ENTRYPOINT fastapi run --port ${FASTAPI_PORT}
