#!/usr/bin/env python3
"""
module task 0
Regex-ing
"""

import re
from typing import List
import logging
import mysql.connector


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
    for field in fields:
        message = re.sub(
            f"{field}=.*?{separator}",
            f"{field}={redaction}{separator}", message
        )
    return message


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
    PII_FIELDS = ["name", "email", "address"]  # Define tus campos aquí
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def get_db():
    """Establish a connection to
    the MySQL database using environment variables"""

    db_username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    if not db_name:
        raise ValueError(
            "The environment variable PERSONAL_DATA_DB_NAME is required."
            )

    try:
        connection = mysql.connector.connect(
            host=db_host, user=db_username,
            password=db_password, database=db_name
        )

        if connection.is_connected():
            print(
                "Successfully connected to the database"
                )
            return connection
        else:
            print("Failed to connect to the database")
            return None
    except Error as err:
        print(f"Error: {err}")
        return None
