


from datetime import timedelta
import datetime
from cachetools import TTLCache


def get_global_ttl_cache(cache = TTLCache(maxsize=2000, ttl=timedelta(hours=2), timer=datetime.now)):
    return cache