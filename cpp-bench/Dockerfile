FROM gcc:14

WORKDIR /app
COPY main.cpp .

RUN g++ -O3 main.cpp -o loopbench

CMD ["./loopbench"]
