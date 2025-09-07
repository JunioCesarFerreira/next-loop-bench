import subprocess
import re
import statistics
import matplotlib.pyplot as plt
import csv

# Number of executions
RUNS = 100

# Containers/languages to benchmark
languages = [
    "go-bench",
    "csharp-bench",
    "java-bench",
    "python-bench",
    "node-bench",
    "c-bench",
    "cpp-bench",
    "rust-bench"
]

# Dictionary to store execution times
results = {lang: [] for lang in languages}

# Regex to capture line: "elapsed time: 201 ms"
pattern = re.compile(r"elapsed time:\s+(\d+)\s+ms", re.IGNORECASE)

for run in range(RUNS):
    print(f"Run {run+1}/{RUNS}")

    # Run docker compose up and capture output
    proc = subprocess.run(
        ["docker", "compose", "up"],
        capture_output=True,
        text=True
    )

    output = proc.stdout.splitlines()

    # Extract times for each language
    for line in output:
        match = pattern.search(line)
        if match:
            time_ms = int(match.group(1))
            for lang in languages:
                if lang in line:  # detect by service name
                    results[lang].append(time_ms)

    # Remove containers for the next run
    subprocess.run(["docker", "compose", "down"], capture_output=True)

# Calculate averages
averages = {lang: statistics.mean(times) for lang, times in results.items() if times}

print("\n=== Average execution times (ms) ===")
for lang, avg in averages.items():
    print(f"{lang}: {avg:.2f} ms")

# --------- Save results to CSV ----------
with open("benchmark_results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["language", "run", "time_ms"])
    for lang in languages:
        for i, t in enumerate(results[lang], start=1):
            writer.writerow([lang, i, t])

print("CSV file saved: benchmark_results.csv")

# --------- Plot 1: line chart with all runs ----------
plt.figure(figsize=(12, 8))
for lang in languages:
    if results[lang]:
        plt.plot(results[lang], label=lang, marker="o", markersize=2, linewidth=1)
plt.xlabel("Run")
plt.ylabel("Time (ms)")
plt.title(f"Benchmark loop 1 billion - {RUNS} runs")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.savefig("benchmark_all_runs.png")

# --------- Plot 2: bar chart with averages ----------
plt.figure(figsize=(12, 8))
langs = list(averages.keys())
times = [averages[lang] for lang in langs]
plt.bar(langs, times)
plt.ylabel("Average time (ms)")
plt.title(f"Benchmark loop 1 billion ({RUNS} runs)")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Rotate X-axis labels for readability
plt.xticks(rotation=45, ha="right")

plt.savefig("benchmark_means.png")
plt.show()
