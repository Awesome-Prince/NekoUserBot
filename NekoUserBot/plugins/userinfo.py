"""
BSD 3-Clause License

Copyright (c) 2022, Awesome-Prince
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from pyrogram import filters

from config import HANDLER, OWNER_ID
from NekoUserBot import neko


@neko.on_message(filters.command("cinfo", prefixes=HANDLER) & filters.user(OWNER_ID))
async def cinfo(_, m):
    reply = m.reply_to_message
    if not reply:
        await m.reply_text("yoo! baka reply to channel")
        return
    if not reply.sender_chat:
        await m.reply_text("yoo! baka reply to channel")
        return
    if reply.sender_chat:
        message = await m.reply_text("information gathering!!!")
        id = reply.sender_chat.id
        reply.sender_chat.type
        name = reply.sender_chat.title
        username = reply.sender_chat.username
        pfp = reply.sender_chat.photo
    if not pfp:
        text = f"✪ **TYPE:** Channel\n\n"
        text += f"✪ **ID:** {id}\n\n"
        text += f"✪ **NAME:** {name}\n\n"
        text += f"✪ **USERNAME:** @{username}\n\n"
        text += f"✪ **MENTION:** [link](t.me/{username})"
        await m.reply_text(text)
        await message.delete()
        return
    image = reply.sender_chat.photo
    if image:
        photo = await neko.download_media(image.big_file_id)
        text = f"✪ **TYPE:** Channel\n\n"
        text += f"✪ **ID:** {id}\n\n"
        text += f"✪ **NAME:** {name}\n\n"
        text += f"✪ **USERNAME:** @{username}\n\n"
        text += f"✪ **MENTION:** [link](t.me/{username})"
        await m.reply_photo(photo=photo, caption=(text))
        await message.delete()


no_reply_user = """ ╒═══「 Appraisal results:」

**ɪᴅ**: `{}`
**ᴅᴄ**: `{}`
**ғɪʀsᴛ ɴᴀᴍᴇ**: {}
**ᴜsᴇʀɴᴀᴍᴇ**: @{}
**ᴘᴇʀᴍᴀʟɪɴᴋ**: {}
**ᴜsᴇʀʙɪᴏ**: {}

**Meet Me Here🙈 @Besties_XD ✨🥀**
"""


@neko.on_message(filters.command("info", prefixes=HANDLER) & filters.user(OWNER_ID))
async def info(_, m):
    m.reply_to_message
    if len(m.command) < 2:
        await m.reply_text("ɢɪᴠᴇ ᴍᴇ ɪᴅ")
        return
    id_user = m.text.split(" ")[1]
    msg = await m.reply_text("ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɢᴀᴛʜᴇʀɪɴɢ!")
    info = await neko.get_chat(id_user)
    if info.photo:
        file_id = info.photo.big_file_id
        photo = await neko.download_media(file_id)
        user_id = info.id
        first_name = info.first_name
        username = info.username
        user_bio = info.bio
        dc_id = info.dc_id
        user_link = f"[link](tg://user?id={user_id})"
        await m.reply_photo(
            photo=photo,
            caption=no_reply_user.format(
                user_id, dc_id, first_name, username, user_link, user_bio
            ),
        )
    elif not info.photo:
        user_id = info.id
        first_name = info.first_name
        username = info.username
        user_bio = info.bio
        dc_id = info.dc_id
        user_link = f"[link](tg://user?id={user_id})"
        await m.reply_text(
            text=no_reply_user.format(
                user_id, dc_id, first_name, username, user_link, user_bio
            )
        )
    await msg.delete()
