use std::time::Instant;

fn main() {
    const N: i64 = 1_000_000_000;
    let start = Instant::now();
    let mut sum: i64 = 0;
    for i in 0..N {
        sum += i;
    }
    let elapsed = start.elapsed().as_nanos();
    println!("result: {}", sum);
    println!("elapsed time: {} ns", elapsed);
}
