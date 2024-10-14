#!/usr/bin/env python3
"""
This module has a method that measure the execution time of wait_n
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time of wait_n(n, max_delay)
    and returns the average time per task.

    Args:
        n (int): Number of times to run wait_n.
        max_delay (int): Maximum delay for wait_n.

    Returns:
        float: Average time per wait_n call.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time

    return total_time / n
