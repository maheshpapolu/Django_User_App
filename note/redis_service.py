import redis
from django.conf import settings


class RedisServer:
    def __init__(self):
        self.r = redis.Redis(**settings.REDIS_CONFIG)

    def set(self, key, value):
        """
        set the data
        """
        return self.r.set(key, value)

    def get(self, key):
        """
        get the data from the cache
        """
        return self.r.get(key)
#     key is user for redis
#     value: {note_id:{id:note_id, title, desc}}
