#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
#الملـف حقـوق وكتابـة زلـزال الهيبـه ⤶ @zzzzl1l خاص بسـورس ⤶ 𝙕𝙚𝙙𝙏𝙝𝙤𝙣
#تعـديل بنيـتي 𝙈

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import sudo_cmd

from . import reply_id


@bot.on(admin_cmd(pattern="تويتر ?(.*)"))
@bot.on(sudo_cmd(pattern="تويتر ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ .تويت بالـرد ﮼؏ الرسالـٓھہ للبحث او .تويتر + الرابـط ...𓅫╰**"
        )
    chat = "@ZedTwbot"
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ التحميل ... 🧸🎈**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2007625255)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @ZedTwbot .. ثم اعـد استخدام الامـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)

@bot.on(admin_cmd(pattern="تويت$", outgoing=True))
@bot.on(sudo_cmd(pattern="تويت$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**بالـرد على الرابـط حمبـي 🧸🎈**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**بالـرد على الرابـط حمبـي 🧸🎈**")
        return
    chat = "@ZedTwbot"
    catevent = await edit_or_reply(event, "**╮•⎚ جـارِ التحميل ... 🧸🎈**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2007625255)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**╮•⎚ تحـقق من انـك لم تقـم بحظر البوت @ZedTwbot .. ثم اعـد استخدام الامـر ...🤖♥️**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**🤨💔...؟**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "تويتر": "**اسم الاضافـه : **`تويتر`\
    \n\n**╮•❐ الامـر ⦂ **`.تويت` بالرد على الرابط\
    \n**الشـرح •• **تحميل مقاطـع الفيديـو من تـويتـر\
    \n\n**╮•❐ الامـر ⦂ **`.تويتر` + الرابط \
    \n**الشـرح •• **تحميل مقاطـع الفيديـو من تـويتـر"
    }
)
