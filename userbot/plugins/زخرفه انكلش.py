#๐๐๐๐๐๐ค๐ฃ ยฎ
#ุงููููู ุญูููู ููุชุงุจูุฉ ุฒููุฒุงู ุงูููุจูู โคถ @zzzzl1l ุฎุงุต ุจุณููุฑุณ โคถ ๐๐๐๐๐๐ค๐ฃ
#ูุฃูู ูุฑู ุน ุชููุซูู ุฃูุฑ ุฒุบุฑููู ุชูุจููุฑ ุนุฏุฉ ุฒุบูุงุฑู ุงููููุด ุจููุช ูุงุญุฏ

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.utils import sudo_cmd

from . import reply_id


@bot.on(admin_cmd(pattern="ุฒุบุฑูู ?(.*)"))
@bot.on(sudo_cmd(pattern="ุฒุบุฑูู ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    chat = "@ZedThonbbot"
    catevent = await edit_or_reply(event, "**ุฌูุงุฑู ุงูุฒุบูุฑููู๐๐งธ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1974043654)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @ZedThonbbot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**")
            return
        if response.text.startswith("I can't find that"):
            await catevent.edit("sorry i can't find it")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)

@bot.on(admin_cmd(pattern="ุฒุบุฑูู$", outgoing=True))
@bot.on(sudo_cmd(pattern="ุฒุบุฑูู$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**ุจุงุถุงููุฉ ุงูููููุฉ ุงููุฑุงุฏ ุฒุบุฑูุชูุง ููุฃููุฑ .. ูุซุงู : .ุฒุบุฑูู + ููููู ๐๐งธ.**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**ุจุงุถุงููุฉ ุงูููููุฉ ุงููุฑุงุฏ ุฒุบุฑูุชูุง ููุฃููุฑ .. ูุซุงู : .ุฒุบุฑูู + ููููู ๐๐งธ.**")
        return
    chat = "@ZedThonbbot"
    catevent = await edit_or_reply(event, "**ุจุงุถุงููุฉ ุงูููููุฉ ุงููุฑุงุฏ ุฒุบุฑูุชูุง ููุฃููุฑ .. ูุซุงู : .ุฒุบุฑูู + ููููู ๐๐งธ.**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1974043654)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @ZedThonbbot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**๐คจ๐...ุ**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "ุฒุฎุฑูู ุงูููุด": "`.ุฒุบุฑูู` + ูููู ุงู ุจุงููุฑุฏ ุน ููููู :\
      \n**ุงูุดูุฑุญ โขโข** ุฒุบูุงุฑู ุงููููุด ุชูุจููุฑ ูุงูุทุฑูููู ููุฃูู ููุฑู ุน ุชูููุซูู ุฃูุฑ ูุฒุบุฑู ุนุฏุฉ ุฒุบูุงุฑู ุงููููุด ุจููุช ูุงุญุฏ .. ุงูููู ุญููู ุฒุฏุซูููู#.. . "
    }
)
