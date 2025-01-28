#!/usr/bin/python3
"""
BaseCaching module
"""
from base_caching import BaseCaching

class BaseCache(BaseCaching):
    """
    a class that manage a cache, Inherits
    from BaseCaching
    """

    def put(self, key, item):
        """
        adds an item to cache if both key
        and  item are not None
        """
        if key is None and item is None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from cache by key.
        Args:
            key: the key to look for in the cache
        Returns:
            the value for key if it exists, otherwise None.
        """
        if key not in self.cache_data:
          return self.cache_data[key]
        return None