#๐๐๐๐๐๐ค๐ฃ ยฎ
#ุงููููู ุญูููู ููุชุงุจูุฉ ุฒููุฒุงู ุงูููุจูู โคถ @zzzzl1l ุฎุงุต ุจุณููุฑุณ โคถ ๐๐๐๐๐๐ค๐ฃ


#ุตุฏููุฉ ุฌูุงุฑููู ููุฑูุญ ุงููุฑุญูููุฉ ุฃููู ูุฑูุญ ุงููุฑุญูููุฉ ุฃู ูููุงุฐ


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import sudo_cmd

from . import reply_id


@bot.on(admin_cmd(pattern="ูุฑุขู ?(.*)"))
@bot.on(sudo_cmd(pattern="ูุฑุขู ?(.*)", allow_sudo=True))
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
            event, "**โฎ .ุจูุงุถุงูุฉ ุงุณูู ุงููุงุฑุฆ + || + ุงุณู ุงูุณูุฑุฉ ููุงููุฑ ููุจุญุซ ูุซูุงู :  .ุงูุณุฏูุณ || ุงูููุซุฑ .. ุงููุฑุงุก ูู ุนุจุฏุงูุตูุฏ - ุงูุดุงุทุฑู - ุงูููุดุงูู - ุงููุนูููู - ุงูููุดู - ุงูุบุงูุฏู - ุงูุฏูุณุฑู - ุงูุฏููุงูู - ุงูุนุฌูู - ุงูุนุจุงุฏ๐ซโฐ**"
        )
    chat = "@BBBllbot"
    catevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุณููุฑุฉ ... ๐งธ๐**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2125397049)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @BBBllbot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "ูุฑุขู ูุฑูู": "**ุงุณู ุงูุงุถุงููู : **`ูุฑุขู ูุฑูู`\
    \n\n**โฎโขโ ุงูุงููุฑ โฆ **`.ูุฑุขู` + ุงุณู ุงููุงุฑุฆ + || + ุงุณู ุงูุณูุฑุฉ \
    \n**ุงูุดูุฑุญ โขโข **ุชุญููู ุณููุฑ ุงูููุฑุขู ุงูููุฑูู ุจุตููุช 13 ูุงุฑุฆ ููุชุนูููุงุช ุงุฑุณู .ูุฑุขู"
    }
)
