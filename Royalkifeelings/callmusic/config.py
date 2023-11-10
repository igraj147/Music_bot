from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME: str = getenv("GetStringRobot", "")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
BOT_USERNAME = getenv("@rdxraj_god_robot", "")
BOT_TOKEN = getenv("6826535275:AAFHKWjI4Y4ups2DdOOcLVvCSMtmMt9ThjY", "")
API_ID = int(getenv("26421919", ""))
API_HASH = getenv("3911f3927de69841858b6f84e770875b", "")
GROUP_SUPPORT = getenv("https://t.me/THE_CRAZY_FUN_0", "")