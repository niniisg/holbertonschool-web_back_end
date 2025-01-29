#!/usr/bin/env python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines a LIFO caching system"""

    def __init__(self):
        """Initialize  cache with
        and empty order list
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache
        If the cache exceeds MAX_ITEMS,
        the last inserted item is discarded (LIFO).
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Get an item from the cache by key
        Returns None if key is no in cache
        """
        return self.cache_data.get(key, None)
