#!/usr/bin/env python3
"""
module task 0
Regex-ing
"""

import re
from typing import List
import logging


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Args:
        This function takes a list of fields,
        redacts their values in a given log message
    Returns:
        A string with the specified fields redacted.
    """
    for f in fields:
        message = re.sub(f"{f}=.*?{separator}",
                         f"{f}={redaction}{separator}", message)

        import logging


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter the record and redact specified fields."""
        return filter_datum(
            self.fields, self.REDACTION, super().format(record), self.SEPARATOR
        )


def get_logger() -> logging.Logger:
    """function that returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger