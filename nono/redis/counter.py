from typing import Dict
from nono.domain.interfaces import Counter

class RedisCounter(Counter):
    def __init__(self, redis_client):
        self.redis_client = redis_client

    async def increment(self, counter_set: str, key: str) -> None:
        await self.redis_client.zincrby(counter_set, 1, key)

    async def decrement(self, counter_set: str, key: str) -> None:
        await self.redis_client.zincrby(counter_set, -1, key)

    async def top(self, counter_set: str, start: int, stop: int) -> Dict[str, int]:
        return await self.redis_client.zrevrange(counter_set, start, stop, withscores=True)
