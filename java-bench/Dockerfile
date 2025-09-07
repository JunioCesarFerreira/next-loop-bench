FROM openjdk:17

WORKDIR /app
COPY src ./src

# Compila com javac
RUN mkdir -p out && javac -d out src/main/java/bench/LoopBench.java

# Executa o programa
CMD ["java", "-cp", "out", "bench.LoopBench"]
