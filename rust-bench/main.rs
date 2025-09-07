use std::time::Instant;

fn main() {
    const N: i64 = 100_000_000;
    let start = Instant::now();
    let mut sum: i64 = 0;
    for i in 0..N {
        sum += i;
    }
    let elapsed = start.elapsed().as_millis();
    println!("result: {}", sum);
    println!("elapsed time: {} ms", elapsed);
}
