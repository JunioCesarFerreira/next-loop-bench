package bench;

public class LoopBench {

    private static final int N = 100_000_000;

    public static void main(String[] args) {
        long start = System.currentTimeMillis();
        long sum = 0;
        for (int i = 0; i < N; i++) {
            sum += i;
        }
        long end = System.currentTimeMillis();
        System.out.println("result: " + sum);
        System.out.println("elapsed time: " + (end - start) + " ms");
    }
}
