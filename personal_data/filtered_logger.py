#!/usr/bin/env python3
"""
module task 0
Regex-ing
"""

import re

"""
module for readacting sensitive
information in log messages
"""


def filter_datum(fields, redaction, message, separator):
    """
    Args:
        This function takes a list of fields,
        redacts their values in a given log message
    Returns:
        A string with the specified fields redacted.
    """
    return re.sub(
        rf'({"|".join(fields)})=[^{separator}]*',
        lambda m: f"{m.group(1)}={redaction}",
        message,
    )
