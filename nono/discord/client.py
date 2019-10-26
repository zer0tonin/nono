import logging

from discord.ext.commands import Bot

from nono.discord.register_interfaces import register_interfaces
from nono.domain.purge import delete_last_messages

logger = logging.getLogger(__name__)

register_interfaces()
client = Bot(command_prefix="!")  # pylint: disable=invalid-name


@client.event
async def on_ready():
    logger.info("We have logged in as {0.user}".format(client))


@client.command(name="purge")
async def purge(ctx, *args):
    deleted = await delete_last_messages(ctx.channel, ctx.message, int(args[0]))
    await ctx.send("Deleted {0} messages".format(deleted))
