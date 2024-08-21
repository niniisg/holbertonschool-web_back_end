#!/usr/bin/env python3
"""
this module collects 10 random numbers
using async comprohension
"""
import asyncio
from typing import List

async_generator = __import__("0-async_generator").async_generator
"""
this coroutine collects numbers from async_generator
function using async_comprehension
"""


async def async_comprehension() -> List[float]:
    return [nums async for nums in async_generator()]
