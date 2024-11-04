from operator import add
import os
import logging


# import dotenv
# dotenv.load_dotenv()



from logging.handlers import RotatingFileHandler

#force user to join your backup channel leave 0 if you don't need.
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002188876691"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002362235577"))

if FORCE_SUB_CHANNEL > FORCE_SUB_CHANNEL2:
    temp = FORCE_SUB_CHANNEL2 
    FORCE_SUB_CHANNEL2 = FORCE_SUB_CHANNEL
    FORCE_SUB_CHANNEL = temp

#bot stats
BOT_STATS_TEXT = os.environ.get("BOTS_STATS_TEXT","<b>𝙱𝙾𝚃 𝚄𝙿𝚃𝙸𝙼𝙴 </b>\n{uptime}")
#send custom message when user interact with bot
USER_REPLY_TEXT = os.environ.get("USER_REPLY_TEXT", "❌ 𝙿𝚕𝚎𝚊𝚜𝚎 𝙰𝚟𝚘𝚒𝚍 𝙳𝚒𝚛𝚎𝚌𝚝 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜. 𝙸'𝚖 𝚆𝚘𝚛𝚔𝚒𝚗𝚐 𝙵𝚘𝚛 𝙾𝚗𝚕𝚢  @Team_Originals")

#your bot token here from https://telegram.me/BotFather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "") 
#your api id from https://my.telegram.org/apps
APP_ID = int(os.environ.get("APP_ID", "20071888"))
#your api hash from https://my.telegram.org/apps
API_HASH = os.environ.get("API_HASH", "1c4cb9d94b23282abd9ae2a87a521b53")
#your channel_id from https://t.me/MissRose_bot by forwarding dummy message to rose and applying command `/id` in reply to that message
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002216311890"))
#your id of telegram can be found by https://t.me/MissRose_bot with '/id' command
OWNER_ID = int(os.environ.get("OWNER_ID", "7840665125"))
#port set to default 8080
PORT = os.environ.get("PORT", "6106")
#your database url mongodb only You can use mongo atlas free cloud database
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Dam:aloksingh@cluster0.6z0hq.mongodb.net/?retryWrites=true&w=majority")
#your database name
DB_NAME = os.environ.get("DB_NAME", "filesharexbot")

#for creating telegram thread for bot to improve performance of the bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
#your start default command message.
START_MSG = os.environ.get("START_MESSAGE", "𝙷𝚎𝚕𝚕𝚘 {first}\n\n𝙸 𝙲𝚊𝚗 𝚂𝚝𝚘𝚛𝚎 𝙿𝚛𝚒𝚟𝚊𝚝𝚎 𝙵𝚒𝚕𝚎𝚜 𝚒𝚗 𝚂𝚙𝚎𝚌𝚒𝚏𝚒𝚎𝚍 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝚊𝚗𝚍 𝚘𝚝𝚑𝚎𝚛 𝚞𝚜𝚎𝚛𝚜 𝚌𝚊𝚗 𝚊𝚌𝚌𝚎𝚜𝚜 𝙿𝚛𝚒𝚟𝚊𝚝𝚎 𝙵𝚒𝚕𝚎𝚜 𝙵𝚛𝚘𝚖 𝚊 𝚂𝚙𝚎𝚌𝚒𝚊𝚕 𝙻𝚒𝚗𝚔....!\n\n𝙿𝚘𝚠𝚎𝚛𝚎𝚍 𝙱𝚢 @Team_Originals 🔥")
#your telegram tag without @
OWNER_TAG = os.environ.get("OWNER_TAG", "Kill_Owner")
#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "0"))


#Shortner (token system) 
"""
some token verification sites
https://dashboard.shareus.io/
"""

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
USE_SHORTLINK = True if os.environ.get('USE_SHORTLINK', "TRUE") == "TRUE" else False 
# only shareus service known rightnow rest you can test on your own
SHORTLINK_API_URL = os.environ.get("SHORTLINK_API_URL", "Modijiurl.com")
# SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "6f53c862c70eefb04d8f8d18953100d35ebc066c")
#use this key if not working ☠️ (jokin!!)
SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "6f53c862c70eefb04d8f8d18953100d35ebc066c")
#add your custom time in secs for shortlink expiration.
# 24hr = 86400
# 12hr = 43200
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', "57600")) # Add time in seconds
#put TRUE if you want shortner in every link generated by the bot.
U_S_E_P = True if (True if os.environ.get('U_S_E_P', "TRUE") == "TRUE" else False) and (USE_SHORTLINK) else False
#Tutorial video for the user of your shortner on how to download.
TUT_VID = os.environ.get("TUT_VID","https://t.me/how_to_hentai/18")





#Payment to remove the token system
#put TRUE if you want this feature
USE_PAYMENT = True if (True if os.environ.get("USE_PAYMENT", "TRUE") == "TRUE" else False) and (USE_SHORTLINK) else False
#UPI ID
UPI_ID = os.environ.get("UPI_ID", "Adk To Owner For Qr)
#UPI QR CODE IMAGE
UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", "")
#SCREENSHOT URL of ADMIN for verification of payments
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/{OWNER_TAG}")
#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "30")
#1 Month
PRICE2 = os.environ.get("PRICE2", "80")
#3 Month
PRICE3 = os.environ.get("PRICE3", "200")
#6 Month
PRICE4 = os.environ.get("PRICE4", "350")
#1 Year
PRICE5 = os.environ.get("PRICE5", "600")



#force message for joining the channel
FORCE_MSG = os.environ.get("FORCE_MSG", "𝚂𝚘𝚛𝚛𝚢 𝙳𝚞𝚍𝚎 𝚈𝚘𝚞 𝙽𝚎𝚎𝚍 𝚃𝚘 𝙹𝚘𝚒𝚗 𝚃𝚑𝚎𝚜𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕𝚜</b>\n\n<b>𝚂𝚘 𝙿𝚕𝚎𝚊𝚜𝚎 𝙲𝚕𝚒𝚌𝚔 𝙱𝚕𝚘𝚠 𝚃𝚘 𝙹𝚘𝚒𝚗 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 🔥</b>")
#custom caption 
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>None</b>")
#protected content so that no files can be sent from the bot to anyone. recommended False
# TRUE for yes FALSE if no
PROTECT_CONTENT = True if os.environ.get("PROTECT_CONTENT", "True") == "TRUE" else False
#used if you dont need buttons on database channel.
# True for yes False if no
DISABLE_CHANNEL_BUTTON = True if os.environ.get("DISABLE_CHANNEL_BUTTON", "TRUE") == "TRUE" else False
#you can add admin inside the bot(bug right now will fix later)

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7350721166").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")




#no need to add anything from now on

ADMINS.append(OWNER_ID)


LOG_FILE_NAME = "logs.txt"
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
