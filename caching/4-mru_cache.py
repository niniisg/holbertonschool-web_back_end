#!/usr/bin/python3
"""
MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    defines a MRUCache system
    """
    def __init__(self):
        """
        Initializes the MRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds or updates an item in the cache.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.order.pop()
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Retrieves an item from the cache
        """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
