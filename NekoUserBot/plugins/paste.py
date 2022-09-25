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

import os
import socket
from asyncio import get_running_loop
from functools import partial

import aiofiles
import requests
from pyrogram import filters
from requests import post

from config import HANDLER, OWNER_ID
from NekoUserBot import neko


def spacebin(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"


def _netcat(host, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096).decode("utf-8").strip("\n\x00")
        if not data:
            break
        return data
    s.close()


async def ezup(content):
    loop = get_running_loop()
    link = await loop.run_in_executor(None, partial(_netcat, "ezup.dev", 9999, content))
    return link


HASTEBIN_URL = "https://www.toptal.com/developers/hastebin/documents"
HASTEBIN = "https://www.toptal.com/developers/hastebin/{}"


@neko.on_message(filters.command("paste", prefixes=HANDLER) & filters.user(OWNER_ID))
async def paste(_, m):
    reply = m.reply_to_message
    if not reply:
        wrong_format = """ **Something You did wrong read the rules of paste:**\n
        ~ Only text files or text only paste.
        ~ Text file Only support lower then 1mb.
        ~ You did Verything right but you got this msg most report on SupportChat
        """
        await m.reply_text(wrong_format)
    if reply.document:
        doc = await m.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            file_text = await f.read()
        os.remove(doc)
        spacebin_url = spacebin(file_text)
        link = await ezup(file_text)
        caption = f"[SPACEBIN]({spacebin_url}) | [EZUP.DEV]({link})"
        await m.reply_text(text=caption, disable_web_page_preview=True)
    elif reply.text or reply.caption:
        text = reply.text or reply.caption
        spacebin_url = spacebin(text)
        link = await ezup(text)
        key = requests.post(
            HASTEBIN_URL,
            data=text.encode("UTF-8"),
        ).json()
        key = key.get("key")
        url = HASTEBIN.format(key)
        caption = f"[SPACEBIN]({spacebin_url}) | [EZUP.DEV]({link})\n         [HASTEBIN]({url})"
        await m.reply_text(text=caption, disable_web_page_preview=True)
