FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Instala Java + Maven
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk maven && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY src ./src
COPY pom.xml .

# Compila
RUN mvn -q clean package -DskipTests

CMD ["java", "-cp", "target/classes", "bench.LoopBench"]
