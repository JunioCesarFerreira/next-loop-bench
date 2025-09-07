# Benchmark Report: Go vs Java (Initial Experiment)

## Experiment Setup

This initial experiment compared the execution time of a **1,000,000,000-iteration loop** implemented in **Go** and **Java**, both running inside identical Docker containers based on Ubuntu.

### Host System Information

The benchmarks were executed on the following host:

* **Operating System**: Ubuntu 22.04.5 LTS (Jammy Jellyfish)
* **Kernel**: 5.15.167.4-microsoft-standard-WSL2
* **Environment**: WSL2 on Windows 10

#### CPU

* Model: Intel(R) Core(TM) i7-10510U CPU @ 1.80GHz
* Architecture: x86\_64
* Cores: 4 (8 threads, Hyper-Threading enabled)
* Base frequency: \~1.8 GHz (reported \~2.3 GHz during measurement)
* Cache: 128 KiB L1d, 128 KiB L1i, 1 MiB L2, 8 MiB L3

#### Memory

* Total RAM: 9.6 GiB
* Free RAM at start: \~3.7 GiB (7.3 GiB available)
* Swap: 3.0 GiB

---

## Container Setup

* **Base image**: Ubuntu 22.04 for both Go and Java containers
* **Go version**: 1.23 (official image)
* **Java version**: OpenJDK 17 (official image)
* **Workload**:

  * Simple loop summing integers from 0 to 1,000,000,000
  * Elapsed time measured in milliseconds using system clock
  * Final result printed to avoid dead-code elimination

---

## Results

From the attached execution log:

* **Go**

  * Result: `499999999500000000`
  * Elapsed time: **1112 ms**

* **Java**

  * Result: `499999999500000000`
  * Elapsed time: **1121 ms**

---

## Discussion

* Both Go and Java produced identical results for the summation.
* Execution times were **very close (\~1.1 seconds)**, with Go slightly faster in this run.
* The similarity highlights that for CPU-bound integer loops of this type, both runtimes achieve comparable performance when compiled/JIT-optimized.
* Results should not be generalized beyond this narrow case; real applications involve memory access, concurrency, and runtime overheads that can affect performance differently.

---

## Next Steps

* Extend benchmarks to **C, C++, Rust, Python, C#, and Node.js**, using the same containerized setup.
* Repeat runs multiple times (e.g., 100) to compute **average and variance**.
* Capture and record **host parameters** for each experiment to ensure reproducibility.
* Compare results across native (C, C++, Rust) and managed (Go, Java, .NET, Node.js, Python) runtimes.

