import logging

from discord.ext.commands import Bot

logger = logging.getLogger(__name__)

client = Bot(command_prefix="!")


@client.event
async def on_ready():
    logger.info("We have logged in as {0.user}".format(client))


@client.command(name="test")
async def say_hello(ctx, *args):
    sentence = " ".join(args)
    await ctx.send(sentence)
