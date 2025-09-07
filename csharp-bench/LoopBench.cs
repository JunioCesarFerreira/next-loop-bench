using System;
using System.Diagnostics;

class LoopBench
{
    const long N = 1_000_000_000;

    static void Main()
    {
        var sw = Stopwatch.StartNew();
        long sum = 0;
        for (long i = 0; i < N; i++)
        {
            sum += i;
        }
        sw.Stop();
        Console.WriteLine($"result: {sum}");
        Console.WriteLine($"elapsed time: {sw.ElapsedMilliseconds} ms");
    }
}
