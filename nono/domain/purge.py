import logging

from nono.domain.interfaces import Channel, Message, User


logger = logging.getLogger(__name__)


async def delete_last_messages(channel: Channel, action_trigger: Message, limit: int) -> int:
    """
    Deletes the last few messages, excluding the message who triggered the action
    """
    ctr = 0
    async for message in channel.history(limit=limit + 1):
        if (
            (message.author.id == action_trigger.author.id
            and message.content == action_trigger.content)
        ):
            continue
        logger.info("Deleting message {0.content}".format(message))
        await message.delete()
        ctr = ctr + 1
    return ctr
