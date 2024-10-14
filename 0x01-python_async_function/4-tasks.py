#!/usr/bin/env python3
"""
This module contains the task_wait_n function.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay for task_wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    # Create a list of tasks for concurrent execution
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Gather results as tasks complete
    delay_list = [await task for task in asyncio.as_completed(tasks)]

    return delay_list
