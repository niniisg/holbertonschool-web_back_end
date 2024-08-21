#!/usr/bin/env python3
import asyncio
import time
"""
this module measure the runtime of executing
async_comprehension four times in parallel
"""
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    this coroutine measure the time taken to
    complete all four coroutines and returns total
    runtimes
    """
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.perf_counter()
    start_time = time.perf_counter()
    return end_time - start_time
