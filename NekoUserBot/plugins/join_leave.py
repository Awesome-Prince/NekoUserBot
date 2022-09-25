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


@neko.on_message(filters.command("join", prefixes=HANDLER) & filters.user(OWNER_ID))
def join_chat(_, m):
    if len(m.command) < 2:
        m.reply_text("ɢɪᴠᴇ ᴀ ᴊᴏɪɴ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪɴᴠɪᴛᴇ  ʟɪɴᴋ")
        return
    link = m.text.split(" ")[1]
    neko.join_chat(link)
    chat = neko.get_chat(link)
    name = chat.title
    m.reply_text(f"Successfully joined {name}")


@neko.on_message(filters.command("leave", prefixes=HANDLER) & filters.user(OWNER_ID))
def leave_chat(_, m):
    if len(m.command) < 2:
        m.reply_text("ɢɪᴠᴇ ᴀ ʟᴇғᴛ ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪɴᴠɪᴛᴇ  ʟɪɴᴋ")
        return
    link = m.text.split(" ")[1]
    neko.leave_chat(link)
    chat = neko.get_chat(link)
    name = chat.title
    m.reply_text(f"Successfully left {name}")
