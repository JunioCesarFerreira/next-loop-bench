FROM gcc:14

WORKDIR /app
COPY loop_bench.c .

RUN gcc -O3 main.c -o loopbench

CMD ["./loopbench"]
