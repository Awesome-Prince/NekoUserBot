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


@neko.on_message(filters.command("write", prefixes=HANDLER) & filters.user(OWNER_ID))
async def write(_, message):
    if len(message.command) < 2:
        return await message.reply_text("ᴘʟᴢ ɢɪᴠᴇ ᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ ғɪʀsᴛ ")
    m = await message.reply_text("ᴡʀɪᴛɪɴɢ...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("ᴜᴘʟᴏᴀᴅɪɴɢ...")
    await m.delete()
    await message.reply_photo(hand, caption="**Meet Me Here🙈 @Besties_XD ✨🥀**")
