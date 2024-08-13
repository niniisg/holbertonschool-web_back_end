#!/usr/bin/env python3


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the product of it and the multiplier.
    """

    def mult(x: float) -> float:
        """
        Multiplies the input by the multiplier.

        Args:
            x (float): The number to be multiplied.

        Returns:
            float: The product of x and the multiplier.
        """
        return x * multiplier

    return mult
