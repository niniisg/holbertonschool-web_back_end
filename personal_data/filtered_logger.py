#!/usr/bin/python3
"""
module task 0
Regex-ing
"""

import re
import logging

"""
module for readacting sensitive
information in log messages
"""


def filter_datum(
    fields: list[str], redaction: str, message: str, separator: str
) -> str:
    """
    redacts specified fields in a message
    """
    for field in fields:
        message = re.sub(
            field + "=.*" + separator, field + "=" + redaction + separator, message
        )

    return message
