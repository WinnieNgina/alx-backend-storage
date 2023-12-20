#!/usr/bin/env python3
"""
Cache class
"""
import redis
import uuid
from typing import Union, Optional, Callable


def decode_utf8(data):
    """Converts bytes too strings"""
    return data.decode("utf-8")


class Cache:
    def __init__(self):
        """creates a connection with db and clears cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates key and stores data in db"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->
    Union[str, bytes, int, float, None]:
        """Retrieves data from db and calls function if provided"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieves data as a str from db"""
        return self.get(key, fn=decode_utf8)

    def get_int(self, key: int) -> Optional[int]:
        """Retrieves data from db as int"""
        result self.get(key, fn=int)
