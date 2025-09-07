import subprocess
import re
import statistics
import matplotlib.pyplot as plt

# Número de execuções
RUNS = 10

# Containers/languages que esperamos
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

# Dicionário para armazenar tempos
results = {lang: [] for lang in languages}

# Regex para capturar linha: "elapsed time: 201 ms"
pattern = re.compile(r"elapsed time:\s+(\d+)\s+ms", re.IGNORECASE)

for run in range(RUNS):
    print(f"Run {run+1}/{RUNS}")

    # Executa docker compose up e captura saída
    proc = subprocess.run(
        ["docker", "compose", "up"],
        capture_output=True,
        text=True
    )

    output = proc.stdout.splitlines()

    # Extrai tempos de cada linguagem
    for line in output:
        match = pattern.search(line)
        if match:
            time_ms = int(match.group(1))
            for lang in languages:
                if lang in line:  # detecta pelo nome do serviço
                    results[lang].append(time_ms)

    # Remove containers para próxima rodada
    subprocess.run(["docker", "compose", "down"], capture_output=True)

# Calcular médias
averages = {lang: statistics.mean(times) for lang, times in results.items() if times}

print("\n=== Médias de execução (ms) ===")
for lang, avg in averages.items():
    print(f"{lang}: {avg:.2f} ms")

# --------- Gráfico 1: linhas com todas as execuções ----------
plt.figure(figsize=(10, 6))
for lang in languages:
    if results[lang]:
        plt.plot(results[lang], label=lang, marker="o", markersize=2, linewidth=1)
plt.xlabel("Execução")
plt.ylabel("Tempo (ms)")
plt.title(f"Benchmark loop 1 bilhão - {RUNS} execuções")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.savefig("benchmark_all_runs.png")

# --------- Gráfico 2: barras com médias ----------
plt.figure(figsize=(8, 5))
langs = list(averages.keys())
times = [averages[lang] for lang in langs]
plt.bar(langs, times)
plt.ylabel("Tempo médio (ms)")
plt.title(f"Benchmark loop 1 bilhão ({RUNS} execuções)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("benchmark_means.png")

plt.show()
