#include <stdio.h>
#include <time.h>
#include <stdint.h>

int main() {
    const long long N = 1000000000LL;
    long long sum = 0;

    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);

    for (long long i = 0; i < N; i++) {
        sum += i;
    }

    clock_gettime(CLOCK_MONOTONIC, &end);

    long long elapsed_ns = 
        (end.tv_sec - start.tv_sec) * 1000000000LL +
        (end.tv_nsec - start.tv_nsec);

    printf("result: %lld\n", sum);
    printf("elapsed time: %lld ns\n", elapsed_ns);

    return 0;
}
