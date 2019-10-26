import logging
import yaml

from nono.discord.client import client

logger = logging.getLogger(__name__)


def run():
    with open("config/config.yml", "r") as stream:
        try:
            config = yaml.safe_load(stream)
            logging.basicConfig(level=config["logging_level"])
            logger.info("Running the client")
            client.run(config["token"])
        except yaml.YAMLError:
            logger.exception("Failed to parse config")
            exit(1)
