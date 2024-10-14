#!/usr/bin/env python3
"""
This module contains a method that returns asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio Task for the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: A task object wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
