#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
#الملـف حقـوق زلـزال الهيبـه ⤶ @zzzzl1l خاص بسـورس ⤶ 𝙕𝙚𝙙𝙏𝙝𝙤𝙣
#الملف متعوب عليه So تخمط وماتذكـر المصـدر == اهينـك

#هه

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


@bot.on(admin_cmd(pattern="لايكي$", outgoing=True))
@bot.on(sudo_cmd(pattern="لايكي$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**```بالـرد على الرابـط حمبـي 🧸🎈```**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**```بالـرد على الرابـط حمبـي 🧸🎈```**")
        return
    chat = "@AlhibaBOT"
    catevent = await edit_or_reply(event, "**╮ ❐ جـارِ التحميـل من لايكـي انتظـر قليلاً  ▬▭... 𓅫╰**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2032675672)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**❈╎تحـقق من انـك لم تقـم بحظـر البوت @AlhibaBOT .. ثم اعـد استخدام الامـر ...🤖♥️**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**🤨💔...؟**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "لايكي": "**اسم الاضافـه : **`لايكي`\
    \n\n**╮•❐ الامـر ⦂ **`.لايكي` بالرد على الرابط\
    \n**الشـرح •• **تحميل مقاطـع الفيديـو من لايكـي"
    }
)
