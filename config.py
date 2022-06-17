## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgDB6QEbDGwT6DJKdfmEnqdw_7maAk9uNsfEA80oA7TfPPYtuGWmCUKe-pj-w1YJp4mu2t8f3_yrz19eR7aLNo_rp2luDmFtx53VASIDY7v6uU-JbTe9BHbIZSNIVyHIBHalNgKXydCnLgvZSqYc-cI2lz-P5F73U_OgYt4tBL0z0EZ8_GViugx7m_MuKgOO11mN-Fh1nLYIxGaqtSShG36Je-aQ48LfPSdUYTuniNne7LmnZnKuIe9qjrP7DQ9R3Eo1cim6PxMqMsxwcKPEWzf4aE6-tzJR6EIOOAM2x1DzwndyPoTJl855M7YbmelFg0Lc-01EpWHgw2sui78Us33fAAAAATAIg2IA")
BOT_TOKEN = getenv("BOT_TOKEN", "5425300563:AAHlhgs1U6hk5JEFHzdRS9YaBhkuXR5ZUL4")
BOT_NAME = getenv("BOT_NAME", "Noor ")
API_ID = int(getenv("API_ID", "11773321"))
API_HASH = getenv("API_HASH", "44fba40abd026c0f44ac6354ab23e8e1")
OWNER_NAME = getenv("OWNER_NAME", "hassan")
OWNER_USERNAME = getenv("OWNER_USERNAME", "D_bb_D")
ALIVE_NAME = getenv("ALIVE_NAME", "HASSAN")
BOT_USERNAME = getenv("BOT_USERNAME", "D_JJ_D_bot")
OWNER_ID = getenv("OWNER_ID", "5392120374")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "D_qq_D")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Posts_f")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Posts_f"
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5392120374").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
