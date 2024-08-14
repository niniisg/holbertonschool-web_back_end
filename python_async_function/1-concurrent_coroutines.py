#!/usr/bin/env python3

from typing import List
import asyncio
import random

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    task = []
    for _ in range(n):
        task.append(wait_random(max_delay))
    delay_list = []
    for result in asyncio.as_completed(task):
        delay = await result
        delay_list.append(delay)
        return delay_list
