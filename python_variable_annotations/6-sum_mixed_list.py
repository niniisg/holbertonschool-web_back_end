#!/usr/bin/env python3
"""
this module provides a function that calculates
the sum of list containing int and float
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of the list elements as a float.
    """
    return sum(mxd_lst)
