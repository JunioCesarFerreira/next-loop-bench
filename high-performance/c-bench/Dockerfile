FROM gcc:14

WORKDIR /app
COPY main.c .

RUN gcc -O3 main.c -o loopbench

CMD ["./loopbench"]
