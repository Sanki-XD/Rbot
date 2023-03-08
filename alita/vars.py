from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    APP_ID = int(config("APP_ID", default="23842900"))
    API_HASH = config("API_HASH", default="d21e95895cf2a5b83b0167fdd3b6e541")
    OWNER_ID = int(config("OWNER_ID", default=6190680150))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=-100))
    DEV_USERS = [int(i) for i in config("DEV_USERS", default="").split()]
    SUDO_USERS = [int(i) for i in config("SUDO_USERS", default="").split()]
    WHITELIST_USERS = [int(i) for i in config("WHITELIST_USERS", default="").split()]
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="alita")
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="NirjonWorldMF")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="NixaWorld")
    ENABLED_LOCALES = [str(i) for i in config("ENABLED_LOCALES", default="en").split()]
    WORKERS = int(config("WORKERS", default=16))
    BOT_USERNAME = ""
    BOT_ID = ""
    BOT_NAME = ""


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "6123933672:AAFXNl0ob9-SuGPpUjc8AwfdpPqK5FanqbY"
    APP_ID = 23842900  # Your APP_ID from Telegram
    API_HASH = "d21e95895cf2a5b83b0167fdd3b6e541"  # Your APP_HASH from Telegram
    OWNER_ID = 6190680150  # Your telegram user id
    MESSAGE_DUMP = -1001862524511  # Your Private Group ID for logs
    DEV_USERS = [6190680150]
    SUDO_USERS = [6190680150]
    WHITELIST_USERS = []
    DB_URI = "mongodb+srv://bsdk:betichod@cluster0.fgj1r9z.mongodb.net/?retryWrites=true&w=majority"
    DB_NAME = "alita"
    NO_LOAD = []
    PREFIX_HANDLER = ["!", "/"]
    SUPPORT_GROUP = "NixaWorld"
    SUPPORT_CHANNEL = "NirjonWorldMF"
    ENABLED_LOCALES = ["en"]
    WORKERS = 8
