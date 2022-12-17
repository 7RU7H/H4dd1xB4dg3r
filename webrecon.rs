use futures::executor::ThreadPool;
use futures::future::{join_all, FutureExt};

fn main() {
    // Create a thread pool with 8 worker threads
    let pool = ThreadPool::new().unwrap();

    // Spawn 10 futures onto the thread pool
    let futures = (0..10).map(|i| {
        pool.spawn_ok(async move {
            // Do some work in parallel
            println!("Future {} starting", i);
            // Sleep for a random amount of time to simulate work
            tokio::time::delay_for(std::time::Duration::from_millis(1000)).await;
            println!("Future {} finished", i);
        })
    });

    // Wait for all futures to complete
    join_all(futures).block_on(pool).unwrap();
}

