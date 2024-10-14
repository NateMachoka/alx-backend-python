#!/usr/bin/env python3
"""
This module contains a coroutine that waits for a random delay
then returns the delay count
"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    # create a list of tasks for concurrent execution
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # gather results in ascending order as tasks complete
    delay_list = [await task for task in asyncio.as_completed(tasks)]

    return delay_list
