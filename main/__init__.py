#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("28348052", default=None, cast=int)
API_HASH = config("5e5076c61fb2f3ac908d9281db2d2e2a", default=None)
BOT_TOKEN = config("7177816811:AAEedPaDiZZ5kCfbBVaPQRF56e9nX02RKi4", default=None)
SESSION = config("BQGwjpQAsO4C9KMFcgAfB7ycuN-cxrtvVTsvkKaacU7M1_-9dl1x9gGDAsaeDkga9U_UpswX_IBN8VRsdwWlhu9gCkZrZtoaeyHpoGCJXDlagijPftEkmkRBrK8vEy8yqUhldk-91GG4tHl1BhcQC1KsLRd-W-qqFRQk3LsuxRxuxf1JLQQwFM1y_OzpkXYlYc7_dJAY45mSeryCC3KBOAuIKy2upMNBp9ZetM14TJT1cpgbXRRindrbEsAXFe8eH5ICIn4y5wcGCFW3VmrstCR0I8jwq7gqdqdh09lABqRbRRAqyQ6hgs3y4-OxLf_QEzySEJ2TryC0Si1xp0_91eTljQEo7gAAAAGr1MrrAQ", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
