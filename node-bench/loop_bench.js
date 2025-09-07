const N = 100_000_000;

function main() {
    const start = Date.now();
    let sum = 0n; // BigInt, para não perder precisão
    for (let i = 0; i < N; i++) {
        sum += BigInt(i);
    }
    const end = Date.now();
    console.log("result: " + sum.toString());
    console.log("elapsed time: " + (end - start) + " ms");
}

main();
