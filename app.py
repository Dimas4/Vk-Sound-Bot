from bot.bot import start

from parse_config.parse_config import parse


if __name__ == "__main__":
    token, backend, filename = parse("config", "config.yaml")
    start(token, backend, filename)
