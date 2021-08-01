#!/usr/bin/env python3
"""Encrypting Passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password,
    which is a byte string"""
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validate that the provided password matches
    the hashed password"""
    password = password.encode("utf-8")
    return True if bcrypt.checkpw(password, hashed_password) else False
