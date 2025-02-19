#!/usr/bin/env python3
"""
module task 0
Regex-ing
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Args:
        This function takes a list of fields,
        redacts their values in a given log message
    Returns:
        A string with the specified fields redacted.
    """
    for f in fields:
        message = re.sub(f + "=.*?" + separator,
                         f + "=" + redaction + separator, message)
    return message
