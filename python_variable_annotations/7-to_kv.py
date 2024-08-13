#!/usr/bin/env python3
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key and a value to a tuple where the value is squared.

    Args:
        k (str): The key, which is a string.
        v (Union[int, float]): The value, which can be an integer or a float.

    Returns:
        Tuple[str, float]: A tuple where the first element is the key and the second element is the square of the value as a float.
    """
    return (k, float(v**2))
