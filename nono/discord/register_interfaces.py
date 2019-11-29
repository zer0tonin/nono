from discord import TextChannel, Message, Member, User, Emoji

from nono.redis.counter import Counter

import nono.domain.interfaces as interfaces


def register_interfaces():
    interfaces.Channel.register(TextChannel)
    interfaces.Message.register(Message)
    interfaces.User.register(Member)
    interfaces.User.register(User)
    interfaces.Emoji.register(Emoji)
    interfaces.Counter.register(Counter)
