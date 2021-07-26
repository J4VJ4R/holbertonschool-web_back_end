#!/usr/bin/python3
"""FIFO Cache System Module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO Cache System Class inherited from BaseCaching class
    Args:
        cache_data: dictionary representing cache
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            to_pop = sorted(self.cache_data)[0]
            self.cache_data.pop(to_pop)
            print('DISCARD:', to_pop)

    def get(self, key):
        """Get an item from cache by key"""
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
