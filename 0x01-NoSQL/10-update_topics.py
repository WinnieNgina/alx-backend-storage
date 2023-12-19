#!/usr/bin/env python3
"""function that changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Updates school topics"""
    my_query = {"name": name}
    new_topics = {"$set": {"topics": topics}}
    mongo_collection.update_one(my_query, new_topics)
