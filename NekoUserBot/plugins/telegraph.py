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
from telegraph import upload_file

from config import HANDLER, OWNER_ID
from NekoUserBot import neko


@neko.on_message(filters.command("tm", prefixes=HANDLER) & filters.user(OWNER_ID))
async def tm(_, message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply_text(
            "Reply to a **Media** to get a permanent telegra.ph link."
        )
    if not reply.media:
        return await message.reply_text(
            "Reply to a **Media** to get a permanent telegra.ph link."
        )
    if reply.media:
        msg = await message.reply_text("downloading")
        path = await reply.download()
        await msg.edit("uploading")
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x
    if url.endswith("jpg"):
        await reply.reply_photo(url, caption=f"{url}")
    elif url.endswith("mp4"):
        await reply.reply_animation(url, caption=f"{url}")
    await msg.delete()
