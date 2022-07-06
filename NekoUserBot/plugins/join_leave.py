from NekoUserBot import neko
from pyrogram import filters
from config import ( OWNER_ID, HANDLER) 

@neko.on_message(filters.command("join",prefixes=HANDLER) & filters.user(OWNER_ID))
def join_chat(_, m):
          if len(m.command) < 2:
               m.reply_text("ɢɪᴠᴇ ᴀ ᴊᴏɪɴ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪɴᴠɪᴛᴇ  ʟɪɴᴋ")
               return 
          link =  m.text.split(" ")[1]
          neko.join_chat(link)
          chat = neko.get_chat(link)
          name = chat.title
          m.reply_text(f"Successfully joined {name}")

@neko.on_message(filters.command("leave",prefixes=HANDLER) & filters.user(OWNER_ID))
def leave_chat(_, m):
          if len(m.command) < 2:
               m.reply_text("ɢɪᴠᴇ ᴀ ʟᴇғᴛ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪɴᴠɪᴛᴇ  ʟɪɴᴋ")
               return 
          link =  m.text.split(" ")[1]
          neko.leave_chat(link)
          chat = neko.get_chat(link)
          name = chat.title
          m.reply_text(f"Successfully left {name}")

