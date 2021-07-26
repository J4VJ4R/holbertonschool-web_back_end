#!/usr/bin/python3
"""Basic Cache Module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A Basic Cache System class inherited from BaseCaching
    Args:
        cache_data: dictionary representing the cache
    """
    def put(self, key, item):
        """Add an item to the cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from cache by key"""
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
