package main

import (
	"testing"
)

const N = 1_000_000_000 // 1 bilhão

// Benchmark simples: soma acumulada
func BenchmarkLoop(b *testing.B) {
	for i := 0; i < b.N; i++ {
		sum := 0
		for j := 0; j < N; j++ {
			sum += j
		}
		if sum == -1 { // evita otimização
			b.Fatal("impossível")
		}
	}
}
