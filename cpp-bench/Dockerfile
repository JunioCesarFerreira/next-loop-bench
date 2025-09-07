FROM gcc:14

WORKDIR /app
COPY loop_bench.cpp .

RUN g++ -O3 main.cpp -o loopbench

CMD ["./loopbench"]
