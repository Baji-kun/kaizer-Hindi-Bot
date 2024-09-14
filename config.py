import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6602474937:AAHW2BtaKrVFtJD8J4OtYcUQBodin4anK14")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26977508"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "396589629e6705c592bc7fe891dc6e37")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001941559447"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5957500906"))

# Port
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://bajikun710:8zU61kKtCFuMmmor@zeno.yft7des.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "netflix")

# Force sub channel id, if you want enable force sub
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "-1001969037404"))
FORCE_CHANNEL2 = int(os.environ.get("FORCE_CHANNEL2", "-1001976730504"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "50"))

# Mainly add graph else telegraph link
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/951ce4c5d759ba604d8be.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/951ce4c5d759ba604d8be.jpg")

# Add your text according to you
HELP_TXT = "<b>Hi\nThis is an file sharing bot work for @Animes_Wide\n\n❏ Bot Cammands\n├/start : start the bot\n\nSimply click on link and start the bot join both channels and try again thats it\n\nDeveloped by <a href=https://t.me/Itz_Spike>Spike</a></b>"
ABOUT_TXT = "<b>Hi{first}\n┏━━━━━━━━━━━━━━━\n◈ Owner: <a href=https://t.me/Itz_Spike>Spike</a>\n◈ Anime channel : <a href=https://t.me/Anime_Wide>Anime Wide</a>\n◈ Movie & Series: <a href=https://t.me/+mKXIX38_UpMxOTg1>Netflix</a>\n◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>\n◈ ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a>\n◈ Develop By  : <a href=https://t.me/Itz_Spike>Spike</a>\n┗━━━━━━━━━━━━━━━</b>"

# start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ {first}\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ\n Powered By - @Animes_Wide</b>")
try:
    ADMINS=[6446763201]
    for x in (os.environ.get("ADMINS", "6193451722").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.") 

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\nᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ !!")

# set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ - @Animes_Wide"

ADMINS.append(OWNER_ID)
ADMINS.append(6193451722)

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))
DEL_MSG = "<b>File will be Auto Deleted In {time}, Forward to Saved Messages Now !!</b>"

LOG_FILE_NAME = "filesharingbot.txt"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Hi There My Name is Sahil and if you like this repo make sure to give it a thumbs up and don't Remove my credit....
