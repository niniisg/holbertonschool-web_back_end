#!/usr/bin/env python3
"""
this module will coroutines loop 10 times,
on each iterarion waits 1 secound
and yield a random int between 0, 10
"""
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields
    random integers.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
