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


@neko.on_message(filters.command("id", prefixes=HANDLER) & filters.user(OWNER_ID))
async def id(_, m):
    reply = m.reply_to_message
    _reply = ""
    if not reply:
        no_reply = f"**ʏᴏᴜʀ ɪᴅ**: `{m.from_user.id}`\n\n"
        no_reply += f"**ᴄʜᴀᴛ ɪᴅ**: `{m.chat.id}`\n\n"
        no_reply += f"**ᴍsɢ ɪᴅ**: `{m.id}`"
        await m.reply_text(text=(no_reply))
    if reply.from_user:
        _reply += f"**ʏᴏᴜʀ ɪᴅ**: `{m.from_user.id}`\n\n"
        _reply += f"**ʀᴇᴘʟɪᴇᴅ ɪᴅ**: `{reply.from_user.id}`\n\n"
        _reply += f"**ᴄʜᴀᴛ ɪᴅ**: `{m.chat.id}`\n\n"
        _reply += f"**ʀᴇᴘʟɪᴇᴅ ᴍsɢ ɪᴅ**: `{reply.id}`\n\n"
    if reply.sender_chat:
        _reply += f"\n\n**ᴄʜᴀɴɴᴇʟ  ɪᴅ**: `{reply.sender_chat.id}`\n\n"
    if reply.sticker:
        _reply += f"**sᴛɪᴄᴋᴇʀ ɪᴅ**: `{reply.sticker.file_id}`"
    elif reply.animation:
        _reply += f"**ᴀɴɪᴍᴀᴛɪᴏɴ ɪᴅ**: `{reply.animation.file_id}`"
    elif reply.document:
        _reply += f"**ᴅᴏᴄᴜᴍᴇɴᴛ ɪᴅ**: `{reply.document.file_id}`"
    elif reply.audio:
        _reply += f"**ᴀᴜᴅɪᴏ ɪᴅ**: `{reply.audio.file_id}`"
    elif reply.video:
        _reply += f"**ᴠɪᴅᴇᴏ ɪᴅ**: `{reply.video.file_id}`"
    elif reply.photo:
        _reply += f"**ᴘʜᴏᴛᴏ ɪᴅ**: `{reply.photo.file_id}`"
    await reply.reply_text(_reply)
    await m.delete()


# test
