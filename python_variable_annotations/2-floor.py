#!/usr/bin/env python3
"""
This module provides a function to compute the floor of a float.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of the given float.

    Args:
        n (float): The float number to floor.

    Returns:
        int: The largest integer less than or equal to the given float.
    """
    return math.floor(n)
