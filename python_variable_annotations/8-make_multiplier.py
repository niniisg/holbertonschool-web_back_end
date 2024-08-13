#!/usr/bin/env python3

"""
this module provides a function to create
multiplier functions, that takes a float
as an argument
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Args:
        multiplier (float): The multiplier to use in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns the product of it and the multiplier.
    """

    def multi(m: float) -> float:
        """
        Multiplies the input by the predefined multiplier.

        Args:
            m (float): The number to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return m * multiplier

    return multi
