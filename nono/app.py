import asyncio
import logging
import yaml

from aioredis import create_redis_pool
from discord.ext.commands import Bot

from nono.discord.client import Nono
from nono.domain.reaction_top import ReactionTop
from nono.redis.counter import RedisCounter

logger = logging.getLogger(__name__)

async def start_bot(config):
    logger.info("Running the client")
    redis = await create_redis_pool("redis://{}:{}".format(config["redis"]["host"], config["redis"]["port"]))
    counter = RedisCounter(redis)
    reaction_top = ReactionTop(counter)

    bot = Bot(command_prefix="!")
    bot.add_cog(Nono(bot, reaction_top))
    await bot.start(config["token"])

def run():
    with open("config/config.yml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
            logging.basicConfig(level=config["logging_level"])
            asyncio.run(start_bot(config))

        except yaml.YAMLError:
            logger.exception("Failed to parse config")
            exit(1)
