#!/usr/bin/env python3
"""
This module contains an asynchronous routine that spawns multiple
coroutines and collects their results in a list.
"""

from typing import List
import asyncio
import random

# Import wait_random from the previous Python file
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    tasks = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    delay_list = []
    for result in asyncio.as_completed(tasks):
        delay = await result
        delay_list.append(delay)

    return delay_list
