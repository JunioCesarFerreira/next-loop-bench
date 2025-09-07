FROM golang:1.23

WORKDIR /app
COPY main.go .

# Compila o programa
RUN go build -o loopbench main.go

CMD ["./loopbench"]
