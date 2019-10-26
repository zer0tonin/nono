import asyncio

from unittest.mock import Mock

import pytest

import nono.domain.interfaces as interfaces
from nono.domain.purge import delete_last_messages


class MessageMock(interfaces.Message):
    def __init__(self, author, content):
        self._author = author
        self._content = content
        self.deleted = False

    @property
    def author(self):
        return self._author

    @property
    def content(self):
        return self._content

    async def delete(self):
        await asyncio.sleep(0)
        self.deleted = True


class ChannelMock(interfaces.Channel):
    def __init__(self, messages):
        self.messages = messages

    async def history(self, limit=None):
        limit = -1 * limit
        loop = asyncio.get_running_loop()
        future = loop.create_future()
        future.set_result(None)
        for message in self.messages[limit:]:
            await future
            yield message


@pytest.mark.asyncio
async def test_purge():
    admin = Mock(spec=interfaces.User)
    admin.id.return_value = 1
    legit = Mock(spec=interfaces.User)
    legit.id.return_value = 2
    spammer = Mock(spec=interfaces.User)
    spammer.id.return_value = 3

    messages = [
        MessageMock(legit, "hello"),
        MessageMock(spammer, "SPAM"),
        MessageMock(spammer, "SPAM"),
        MessageMock(spammer, "SPAM"),
        MessageMock(admin, "!purge 3"),
    ]
    channel = ChannelMock(messages)
    await delete_last_messages(channel, messages[-1], 3)

    for message in channel.messages:
        if message.author.id() == 3:
            assert message.deleted
        else:
            assert not message.deleted
