#!/usr/bin/env python3
"""
Async basics in Python task 1
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of delayed float values using wait_random coroutine
    """
    tasks = []
    delays = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    for t in asyncio.as_completed(tasks):
        delays.append(await t)

    return delays
