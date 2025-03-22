#!/usr/bin/env python3
"""
Redis basic operations module
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


class Cache:
    """
    Cache class for storing data in Redis
    """
    def __init__(self):
        """
        Initialize the Cache instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
        
    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Get data from Redis and convert it using the callable fn
        """
        data = self._redis.get(key)
        if data is None:
            return None
        
        if fn:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> str:
        """
        Get a string value from Redis
        """
        return self.get(key, lambda d: d.decode("utf-8"))
    
    def get_int(self, key: str) -> int:
        """
        Get an integer value from Redis
        """
        return self.get(key, int)
    