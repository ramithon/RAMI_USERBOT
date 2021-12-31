#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
#الملـف حقـوق وكتابـة زلـزال الهيبـه ⤶ @zzzzl1l خاص بسـورس ⤶ 𝙕𝙚𝙙𝙏𝙝𝙤𝙣

import asyncio
import base64
import os
import random
import time
from datetime import datetime
from io import BytesIO

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from PIL import Image
from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.functions.messages import SendMediaRequest

from . import make_gif, progress
from . import reply_id

if not os.path.isdir("./temp"):
    os.makedirs("./temp")


@bot.on(admin_cmd(pattern="نوت$", outgoing=True))
@bot.on(sudo_cmd(pattern="نوت$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**```بالـرد على الفيديـو حمبـي 🧸🎈```**")
        return
    chat = "@SYRAPK_CONVERTBOT"
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ التحـويل ... 🧸🎆**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1546534674)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @SYRAPK_CONVERTBOT .. ثم اعـد استخدام الامـر ...🤖♥️**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**🤨💔...؟**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "فيديو نوت": "**اسم الاضافـه : **`فيديو نوت`\
    \n\n**╮•❐ الامـر ⦂ **`.نوت` بالرد على الفيـديـو\
    \n**الشـرح •• **تحـويل الفيديـو الـى فيديـو نـوت"
    }
)
