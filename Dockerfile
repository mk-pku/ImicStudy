FROM python:3.13

WORKDIR /app

ARG UID
ARG GID

RUN groupadd -g $GID -o appgroup && \
    useradd --shell /bin/bash -u $UID -g $GID -o -c "" -m appuser

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt