#!/usr/bin/env python3

import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns the average time per call.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for each call to wait_n.

    Returns:
        float: The average time per call to wait_n.
    """
    start_time = time.perf_counter()
    wait_n(n, max_delay)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time / n
