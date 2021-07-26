#!/usr/bin/python3
"""LRU Cache System Module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A LRU (least recently used) Cache System Class inherited from
    BaseCaching class.

    Args:
        cache_data: dictionary representing cache
        counter: integer, increments when accessing or
            adding an item to the cache.
        ages: dictionary with key:key of cache_data and
            value: current counter value.

    """
    def __init__(self):
        self.counter = 0
        self.ages = {}
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_pop = sorted(self.ages.items(),
                                key=lambda x: x[1])[0][0]
                self.cache_data.pop(to_pop)
                self.ages.pop(to_pop)
                print('DISCARD:', to_pop)

            self.ages[key] = self.counter
            self.counter += 1

    def get(self, key):
        """Get an item from cache by key"""
        if key and key in self.cache_data:
            self.ages[key] = self.counter
            self.counter += 1
            return self.cache_data.get(key)
        return None
