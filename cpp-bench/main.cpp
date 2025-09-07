#include <iostream>
#include <chrono>

int main() {
    const long long N = 100000000LL;
    long long sum = 0;

    auto start = std::chrono::high_resolution_clock::now();
    for (long long i = 0; i < N; i++) {
        sum += i;
    }
    auto end = std::chrono::high_resolution_clock::now();

    auto elapsed_ms = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();

    std::cout << "result: " << sum << std::endl;
    std::cout << "elapsed time: " << elapsed_ms << " ms" << std::endl;

    return 0;
}
