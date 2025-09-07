#include <stdio.h>
#include <time.h>
#include <stdint.h>

int main() {
    const long long N = 100000000LL;
    long long sum = 0;

    clock_t start = clock();
    for (long long i = 0; i < N; i++) {
        sum += i;
    }
    clock_t end = clock();

    double elapsed_ms = (double)(end - start) * 1000.0 / CLOCKS_PER_SEC;

    printf("result: %lld\n", sum);
    printf("elapsed time: %.0f ms\n", elapsed_ms);

    return 0;
}
