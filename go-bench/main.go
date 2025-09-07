package main

import (
	"fmt"
	"time"
)

const N = 100_000_000 // 1 bilhão

func main() {
	start := time.Now()
	var sum int64 = 0
	for i := 0; i < N; i++ {
		sum += int64(i)
	}
	elapsed := time.Since(start).Milliseconds()
	fmt.Printf("result: %d\n", sum)
	fmt.Printf("elapsed time: %d ms\n", elapsed)
}
