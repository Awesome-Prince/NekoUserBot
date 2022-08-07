import os

from pyrogram import filters

from config import HANDLER, OWNER_ID
from NekoUserBot import neko


@neko.on_message(filters.command("rename", prefixes=HANDLER) & filters.user(OWNER_ID))
def rename(_, message):

    try:
        filename = message.text.replace(message.text.split(" ")[0], "")

    except Exception as e:
        print(e)

    if reply := message.reply_to_message:
        x = message.reply_text("Downloading.....")
        path = reply.download(file_name=filename)
        x.edit("Uploading.....")
        message.reply_document(path)
        os.remove(path)
