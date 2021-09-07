#!/usr/bin/env python3
"""Task 9"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs
    """
    id_ = mongo_collection.insert(kwargs)
    return id_
