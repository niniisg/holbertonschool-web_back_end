#!/usr/bin/env python3
from typing import Tuple

"""
this module calculate the start
and end index for pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    retrurns tuple containing the start index and the
    end index for the given pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
