FROM ubuntu:20.04

RUN apt-get update && apt-get install -y --no-install-recommends osmium-tool python3 && \
    rm -rf /var/lib/apt/lists/*
