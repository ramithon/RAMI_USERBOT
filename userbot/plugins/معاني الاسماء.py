#๐๐๐๐๐๐ค๐ฃ ยฎ
#ุงููููู ุญูููู ููุชุงุจูุฉ ุฒููุฒุงู ุงูููุจูู โคถ @zzzzl1l ุฎุงุต ุจุณููุฑุณ โคถ ๐๐๐๐๐๐ค๐ฃ

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import sudo_cmd

from . import reply_id


@bot.on(admin_cmd(pattern="ูุนุงูู ?(.*)"))
@bot.on(sudo_cmd(pattern="ูุนุงูู ?(.*)", allow_sudo=True))
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
            event, "**โฎ .ูุนุงูู + ุงูุงุณูู ... ููุจุญูุซ ุนู ูุนุงููู ุงูุงุณููุงุก ...๐ซโฐ**"
        )
    chat = "@zzznambot"
    catevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุงูุจุญูุซ ุนูู ูุนููู ุงูุงุณูู ... ๐งธ๐**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2045033062)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @zzznambot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)

@bot.on(admin_cmd(pattern="ุตูุงุช ?(.*)"))
@bot.on(sudo_cmd(pattern="ุตูุงุช ?(.*)", allow_sudo=True))
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
            event, "**โฎ .ุตูุงุช + ุงูุงุณูู ... ููุจุญูุซ ุนู ุตูุงุช ุงูุงุณููุงุก ...๐ซโฐ**"
        )
    chat = "@zzzsfbot"
    catevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุงูุจุญูุซ ุนูู ุตููุงุช ุงูุงุณูู ... ๐งธ๐**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2098108665)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @zzzsfbot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "ูุนุงูู ุงูุงุณูุงุก": "**ุงุณู ุงูุงุถุงููู : **`ูุนุงูู ุงูุงุณูุงุก`\
    \n\n**โฎโขโ ุงูุงููุฑ โฆ **`.ูุนุงูู` + ุงูุงุณู \
    \n**ุงูุดูุฑุญ โขโข **ููุจุญูุซ ุนูู ูุนุงููู ุงูุงุณููุงุก\
    \n\n**โฎโขโ ุงูุงููุฑ โฆ **`.ุตูุงุช` + ุงูุงุณู \
    \n**ุงูุดูุฑุญ โขโข **ููุจุญูุซ ุนูู ุตููุงุช ุงูุงุณููุงุก"
    }
)
