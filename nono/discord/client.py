import logging

from discord.ext.commands import Cog, command

from nono.discord.register_interfaces import register_interfaces
from nono.domain.purge import delete_last_messages


logger = logging.getLogger(__name__)

register_interfaces()

class Nono(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        logger.info("We have logged in as {0.user}".format(self.bot))

    @command(name="purge")
    async def purge(self, ctx, *args):
        deleted = await delete_last_messages(ctx.channel, ctx.message, int(args[0]))
        await ctx.send("Deleted {0} messages".format(deleted))
