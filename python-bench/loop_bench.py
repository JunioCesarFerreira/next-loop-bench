import time

N = 1_000_000_000  # 100 milhões

def main():
    start = time.time()
    s = 0
    for i in range(N):
        s += i
    end = time.time()
    elapsed_ms = int((end - start) * 1000)
    print(f"result: {s}")
    print(f"elapsed time: {elapsed_ms} ms")

if __name__ == "__main__":
    main()
