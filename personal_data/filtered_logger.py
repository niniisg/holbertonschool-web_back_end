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
    return re.sub(
        rf'({"|".join(fields)})=[^{separator}]*',
        lambda m: f'{m.group(1)}={redaction}', message
    )
