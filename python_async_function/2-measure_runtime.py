#!/usr/bin/env python3
"""
this module measure the time
in async comprehesion
"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average time taken for
    executing the wait_n coroutine.
    """
    start = time.time()
    wait_n(n, max_delay)
    end = time.time()
    return (end - start) / n
