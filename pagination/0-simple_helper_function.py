#!/usr/bin/env python3
from typing import Tuple

"""
this module calculate the start
and end index for pagination
"""

def index_range(page: int = 1, page_size:int = 10) -> Tuple[int, int]:
    """
    retrurns tuple containing the start index and the
    end index for the given pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
