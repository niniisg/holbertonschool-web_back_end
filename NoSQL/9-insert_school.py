#!/usr/bin/env python3

"""
this module inserts a new document
in a collection
"""

def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a
    collection based on kwargs
    """
    ins = mongo_collection.insert_one(kwargs)
    return ins.inserted_id
