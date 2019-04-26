import asyncio
import logging

from discord.ext.commands import Bot

logger = logging.getLogger(__name__)

client = Bot(command_prefix="!")


@client.event
async def on_ready():
    logger.info("We have logged in as {0.user}".format(client))


async def delete_last_messages(ctx, limit):
    async for message in ctx.channel.history(limit=limit + 1):
        if message.author == ctx.message.author and message.content == ctx.message.content:
            continue
        logger.info("Deleting message {0.content}".format(message))
        await message.delete()


@client.command(name="purge")
async def purge(ctx, *args):
    message = asyncio.create_task(ctx.send("E X T E R M I N A T U S"))
    deletion = asyncio.create_task(delete_last_messages(ctx, int(args[0])))
    await asyncio.gather(message, deletion)
