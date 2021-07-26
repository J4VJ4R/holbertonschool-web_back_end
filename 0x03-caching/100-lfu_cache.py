#!/usr/bin/python3
"""LFU Cache System Module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A LFU (least recently used) Cache System Class inherited from
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
        self.used = {}
        super().__init__()

    def count_used(self, key):
        """Increases value of key by 1 if it exists"""
        if key in self.used:
            self.used[key] += 1
        else:
            self.used[key] = 1

    def put(self, key, item):
        """Add an item to the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                least_used = min(self.used.values())
                for k, _ in sorted(self.ages.items(),
                                   key=lambda x: x[1]):
                    if self.used[k] == least_used:
                        self.cache_data.pop(k)
                        self.ages.pop(k)
                        self.used.pop(k)
                        break
                print('DISCARD:', k)
            self.ages[key] = self.counter
            self.counter += 1
            self.count_used(key)

    def get(self, key):
        """Get an item from cache by key"""
        if key and key in self.cache_data:
            self.ages[key] = self.counter
            self.counter += 1
            self.count_used(key)
            return self.cache_data.get(key)
        return None
