#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU caching system"""

    def __init__(self):
        """
        Initializes the LRUCache with
        an empty order list
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds an item to the cache.
        If the cache is full,
        discards the least recently used item.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.order.pop(0)
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Retrieves an item from the cache,
        marking it as recently used.
        """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
