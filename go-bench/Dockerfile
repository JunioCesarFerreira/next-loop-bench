FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Instala Go
RUN apt-get update && \
    apt-get install -y wget git build-essential && \
    wget https://go.dev/dl/go1.23.0.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.23.0.linux-amd64.tar.gz && \
    rm go1.23.0.linux-amd64.tar.gz

ENV PATH="/usr/local/go/bin:${PATH}"

WORKDIR /app
COPY main.go .

RUN go build -o loopbench main.go

CMD ["./loopbench"]
