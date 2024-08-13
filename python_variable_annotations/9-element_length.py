#!/usr/bin/env python3
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains a sequence from the input and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequences
    (e.g., lists, strings, tuples).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, each containing a
    sequence from the input and its length.
    """
    return [(i, len(i)) for i in lst]
