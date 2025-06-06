FROM eclipse-temurin:24-jdk

WORKDIR /app

ARG UID
ARG GID

RUN groupadd -g $GID -o appgroup && \
	useradd --shell /bin/bash -u $UID -g $GID -o -c "" -m appuser

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER appuser