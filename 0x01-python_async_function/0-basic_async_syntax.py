#!/usr/bin/env python3
"""Async basics in Python task 0"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Generates a random delay between 0 and max_delay"""
    delay: int = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
