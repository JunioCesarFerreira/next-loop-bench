FROM rust:1.81

WORKDIR /app
COPY main.rs .

RUN rustc -O main.rs -o loopbench

CMD ["./loopbench"]
