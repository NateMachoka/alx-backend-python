#!/usr/bin/env python3
"""
This coroutine will execute async_comprehension four times in parallel
uses asyncio.gather
measures the total runtime and returns it.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel
    measure the total runtime.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start_time

    return total_time
