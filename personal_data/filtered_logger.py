#!/usr/bin/env python3
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


import re

def filter_datum(fields, redaction, message, separator):
    return re.sub(
        rf'({"|".join(fields)})=[^{separator}]*',
        lambda m: f'{m.group(1)}={redaction}',
        message
    )