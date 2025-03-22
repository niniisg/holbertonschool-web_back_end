#!/usr/bin/env python3
"""
Redis basic operations module
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many
    times a method is called
    """
    
    @wraps(method)
    def wrapper(*args, **kwargs):
        self = args[0]
        key = method.__qualname__
        self._redis.incr(key)
        return method(*args, **kwargs)
    
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs
    and outputs for a method
    """
    @wraps(method)
    def wrapper(*args, **kwargs):  
        self = args[0]  # Get instance
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
    
        self._redis.rpush(input_key, str(args[1:]))
        result = method(*args, **kwargs)
        self._redis.rpush(output_key, str(result))
        
        return result
    return wrapper





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
    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
        
    def get(self, key: str, fn: Optional[Callable] = None): 
        """
        Get data from Redis and convert
        it using the callable fn
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