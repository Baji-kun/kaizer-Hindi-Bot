import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7741241879:AAHGtb33VOL2T0-NTKCeph_LLHWytzWwx7U")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26634100"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9ea49405d5a93e784114c469f5ce4bbd")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002309655070"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6635547757"))

# Port
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Taki:bot@taki.y0vyy.mongodb.net/?retryWrites=true&w=majority&appName=Taki")
DB_NAME = os.environ.get("DATABASE_NAME", "Kai")

# Force sub channel id, if you want enable force sub
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "0"))
FORCE_CHANNEL2 = int(os.environ.get("FORCE_CHANNEL2", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "50"))

# Mainly add graph else telegraph link
START_PIC = os.environ.get("START_PIC", "https://envs.sh/T14.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/T14.jpg")

# Add your text according to you
HELP_TXT = "<b>Hi\nThis is an file sharing bot work for @Animes_Wide\n\n❏ Bot Cammands\n├/start : start the bot\n\nSimply click on link and start the bot join both channels and try again thats it\n\nDeveloped by <a href=https://t.me/Itz_Spike>Spike</a></b>"
ABOUT_TXT = "<b>Hi{first}\n┏━━━━━━━━━━━━━━━\n◈ Owner: <a href=https://t.me/Itz_Spike>Spike</a>\n◈ Anime channel : <a href=https://t.me/Anime_Wide>Anime Wide</a>\n◈ Movie & Series: <a href=https://t.me/+mKXIX38_UpMxOTg1>Netflix</a>\n◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>\n◈ ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a>\n◈ Develop By  : <a href=https://t.me/Itz_Spike>Spike</a>\n┗━━━━━━━━━━━━━━━</b>"

# start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}\n\nI am a File Store Bot Powered By @Hentaii_Hanime_HEMTAI</b>")

try:
    ADMINS=[6193451722]
    for x in (os.environ.get("ADMINS", "5957500906 7194322981").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Owner list does not contain valid integers.")

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ꜱᴏʀʀʏ, ᴅᴜᴅᴇ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴍʏ ᴄʜᴀɴɴᴇʟꜱ 😔</b>\n\n<b>ꜱᴏ, ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʀʏ ᴀɢᴀɪɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇ ⚡</b>")

# set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ - @Hentaii_Hanime_HEMTAI"

ADMINS.append(OWNER_ID)
ADMINS.append(6193451722)

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "1800"))
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
