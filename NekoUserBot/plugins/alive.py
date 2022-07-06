import time 
import random 
from config import HANDLER, OWNER_ID, neko, ALIVE_TEXT
from pyrogram import filters, __version__ as pyrover
from NekoUserBot import bot, get_readable_time, StartTime



@neko.on_message(filters.command("alive",prefixes=HANDLER) & filters.user(OWNER_ID))
def alive(_, m):
    you = neko.get_me()
    start_time = time.time()
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    uptime = get_readable_time((time.time() - StartTime))
    m.reply_photo(NEKO,caption=ALIVE_TEXT.format(you.mention,pyrover,ping_time,uptime))

      
