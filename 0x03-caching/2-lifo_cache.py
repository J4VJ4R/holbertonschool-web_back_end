#!/usr/bin/python3
"""LIFO Cache System Module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A LIFO Cache System Class inherited from BaseCaching class
    Args:
        last_put: string, stores the last item added to the cache
        cache_data: dictionary representing cache
    """
    def __init__(self):
        self.last_put = ""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_put)
            print('DISCARD:', self.last_put)
        if key:
            self.last_put = key

    def get(self, key):
        """Get an item from cache by key"""
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
