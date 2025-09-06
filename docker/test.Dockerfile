FROM python:3.12-slim

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

COPY ./tests /app/tests

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pytest pytest-mock pytest-cov
