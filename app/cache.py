from cachetools import TTLCache
from app.config import CACHE_TTL_SECONDS

cache = TTLCache(maxsize=100, ttl=CACHE_TTL_SECONDS)