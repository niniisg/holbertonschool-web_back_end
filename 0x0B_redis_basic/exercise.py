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

def replay(method: Callable):
    """
    Display the history of calls of a particular function
    """
    if not hasattr(method, "__self__") or not hasattr(method.__self__, "_redis"):
        print(f"Cannot replay {method.__qualname__}: not a Cache method")
        return
        
    redis_instance = method.__self__._redis 
    method_name = method.__qualname__
    
    calls_count = redis_instance.get(method_name)
    calls_count = calls_count.decode("utf-8") if calls_count else "0"
    
    print(f"{method_name} was called {calls_count} times:")
    
    inputs = redis_instance.lrange(f"{method_name}:inputs", 0, -1)
    outputs = redis_instance.lrange(f"{method_name}:outputs", 0, -1)
    
    for input_data, output_data in zip(inputs, outputs):
        input_str = input_data.decode("utf-8")
        output_str = output_data.decode("utf-8")
        print(f"{method_name}(*{input_str}) -> {output_str}")

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

    @count_calls
    @call_history
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
    
  