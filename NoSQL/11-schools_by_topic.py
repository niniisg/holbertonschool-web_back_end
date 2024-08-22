#!/usr/bin/env python3
"""
this module returns the list
of school with specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Queries the mongo_collection to find
    all schools that have the specified topic.
    """
    return mongo_collection.find({'topics': topic})
