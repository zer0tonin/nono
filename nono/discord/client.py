import logging

from discord.ext.commands import Cog, command

from nono.discord.register_interfaces import register_interfaces
from nono.domain.purge import delete_last_messages


logger = logging.getLogger(__name__)

register_interfaces()

class Nono(Cog):
    def __init__(self, bot, reaction_top):
        self.bot = bot
        self.reaction_top = reaction_top

    @Cog.listener()
    async def on_ready(self):
        logger.info("We have logged in as {0.user}".format(self.bot))

    @Cog.listener()
    async def on_reaction_add(self, reaction, user):
        await self.reaction_top.handle_add(user, reaction.emoji)

    @command(name="purge")
    async def purge(self, ctx, *args):
        deleted = await delete_last_messages(ctx.channel, ctx.message, int(args[0]))
        await ctx.send("Deleted {0} messages".format(deleted))

    @command(name="top")
    async def top(self, ctx, *args):
        top = await self.reaction_top.top(ctx.author)
        await ctx.send(top)
