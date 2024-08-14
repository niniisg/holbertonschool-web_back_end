#!/usr/bin/env python3

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def task_wait_n(max_delay: int) -> List[float]:
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
