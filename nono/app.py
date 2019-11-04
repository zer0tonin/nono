import logging
import yaml

from discord.ext.commands import Bot

from nono.discord.client import Nono

logger = logging.getLogger(__name__)


def run():
    with open("config/config.yml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
            logging.basicConfig(level=config["logging_level"])
            logger.info("Running the client")
            bot = Bot(command_prefix="!")
            bot.add_cog(Nono(bot))
            bot.run(config["token"])
        except yaml.YAMLError:
            logger.exception("Failed to parse config")
            exit(1)
