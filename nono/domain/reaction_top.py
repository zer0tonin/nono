from typing import Dict

from nono.domain.interfaces import User, Emoji, Counter

class ReactionTop:
    def __init__(self, counter: Counter) -> None:
        self.counter = counter

    async def handle_add(self, user: User, emoji: Emoji) -> None:
        counter_set = "emoji:{}".format(user.id)
        await self.counter.increment(counter_set, emoji)

    async def handle_remove(self, user: User, emoji: Emoji) -> None:
        counter_set = "emoji:{}".format(user.id)
        await self.counter.decrement(counter_set, emoji)

    async def top(self, user: User) -> Dict[str, int]:
        counter_set = "emoji:{}".format(user.id)
        raw_top = await self.counter.top(counter_set, 0, 10)
        return [(emoji.decode('utf-8'), score) for emoji, score in raw_top]
