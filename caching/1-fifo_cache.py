#!/usr/bin/python3
"""
FIFO Caching module
Implements FIFO (First In, First Out) caching.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Caching system that follows the FIFO algorithm.

    Attributes:
        order (list): Keeps track of the order keys were added to the cache.
    """

    def __init__(self):
        """Initialize cache and order list."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds an item to the cache.

        If the cache exceeds MAX_ITEMS, the first inserted item is discarded.
        Prints the discarded key.

        Args:
            key (str): Key for the cache item.
            item: Value to store in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """
        Retrieves an item by key.

        Args:
            key (str): Key to retrieve from cache.

        Returns:
            Value of the cache item or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
