#!/usr/bin/env python3
"""Logging Tasks"""
from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """A RedactingFormatter Class
    Args:
        fields: fields in messageto replace with redaction
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filters values in incoming log records using filter_datum.
        Values for fields in fields should be filtered."""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        formatter = logging.Formatter(self.FORMAT)
        return formatter.format(record)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Uses a regex to replace ocurrences of certain field
    values match everything after field plus = until separator
    """
    for field in fields:
        pattern = field + "=.+?(?=abc)*\\" + ";"
        message = re.sub(pattern, field + "=" + redaction + separator, message)
    return message


def get_logger() -> logging.Logger:
    """Creates a logger and returns it"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = logging.Formatter(RedactingFormatter(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to a database"""
    connector = mysql.connector.connect(
        user=os.environ.get("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.environ.get("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.environ.get("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.environ.get("PERSONAL_DATA_DB_NAME"))
    return connector


if __name__ == '__main__':
    connection = get_db()
    cursor = connection.cursor(dictionary=True)
    query = ("SELECT * FROM users")
    cursor.execute(query)
    for row in cursor:
        string = ""
        for key in row:
            string += "{}={}; ".format(key, row[key])
        print(string)
    cursor.close()
    connection.close()
