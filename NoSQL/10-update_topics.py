#!/usr/bin/env python3
"""
this module writes a function that
changes all topics of school
"""


def update_topics(mongo_collection, name, topics):
    """
    updates the topics of school document
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )