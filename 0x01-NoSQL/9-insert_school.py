#!/usr/bin/env python3
"""Inserts a new document to a collection"""


def insert_school(mongo_collection, **kwargs):
    """mongo_collection will be the pymongo collection object
    Returns the new _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
