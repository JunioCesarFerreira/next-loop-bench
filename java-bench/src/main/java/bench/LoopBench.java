package src.main.java.bench;

import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.Scope;
import org.openjdk.jmh.annotations.State;

@State(Scope.Thread)
public class LoopBench {

    private static final int N = 1_000_000_000; // 1 bilhão

    @Benchmark
    public void testLoop() {
        long sum = 0;
        for (int i = 0; i < N; i++) {
            sum += i;
        }
        if (sum == -1) throw new RuntimeException("impossível");
    }
}
