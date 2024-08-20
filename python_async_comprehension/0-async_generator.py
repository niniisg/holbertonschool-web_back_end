#!/usr/bin/env python3

import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields
    random integers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
