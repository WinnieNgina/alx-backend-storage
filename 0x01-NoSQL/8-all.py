#!/usr/bin/env python3
"""lists all documents in a collection"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    :param mongo_collection: Pymongo collection object
    :return: List of documents
    """
    documents = []
    documents = mongo_collection.find()
    return documents
