from . import reply_id as rd
from userbot.tosh import *


WPIC = "https://telegra.ph/file/69eb51863df0bd57d31d7.jpg"
T = "𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 - 𝑺𝑬𝑪𝑹𝑬𝑻 𝑴𝑺𝑮 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⌔∮ قائـمه اوامر الهمسه :** \n⪼ `.الهمسه` لعرض كيفيه ارسال الهمسه من بوتك\n⪼ `.همسه` لارسال همسه عن طريق بوت الهمسه  \n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n𓆩 𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 - [قناة السورس](t.me/ZedThon) 𓆪"

@bot.on(admin_cmd(pattern="م21"))
@bot.on(sudo_cmd(pattern="م21", allow_sudo=True))
async def wspr(kimo):
    await eor(kimo, T)


# Wespr - همسه
@bot.on(admin_cmd(pattern="الهمسه$"))
@bot.on(sudo_cmd(pattern="الهمسه$", allow_sudo=True))
async def kimo(lon):
    if lon.fwd_from:
        return
    ld = await rd(lon)
    if WPIC:
        ics_c = f"**- يمكنك ارسال همسة لعده اشخاص مره واحده**\n**- يمكنك همس ( ملصق - صوره - صوت - متحرك - فيديو ) فقط ارسل كلمة همسه للبوت** @zzll_bot \n**- يوصل اشععار من شاهد همستك فقط اذا كانت الهمسه نص**\n\n**-ميزه ممطروقه بالبوت :**\n**يمكنك عمل همسه بالرد ع الشخص فقط اضف البوت للمجموعه وقم بالرد ع الشخص بكلمة همسه 🧸🎁**\n\n𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 -** @ZedThon"
        ics_c += f"**- قم بنسخ :**\n `@zzll_bot الرساله ثم معرف الشخص`"
        await lon.client.send_file(lon.chat_id, WPIC, caption=ics_c, reply_to=ld)


# Wespr - همسه
@bot.on(admin_cmd(pattern="همسه$"))
@bot.on(sudo_cmd(pattern="همسه$", allow_sudo=True))
async def kimo(lon):
    if lon.fwd_from:
        return
    ld = await rd(lon)
    if WPIC:
        ics_c = f"**- يمكنك ارسال همسة لعده اشخاص مره واحده**\n**- يمكنك همس ( ملصق - صوره - صوت - متحرك - فيديو ) فقط ارسل كلمة همسه للبوت** @zzll_bot \n**- يوصل اشععار من شاهد همستك فقط اذا كانت الهمسه نص**\n\n**-ميزه ممطروقه بالبوت :**\n**يمكنك عمل همسه بالرد ع الشخص فقط اضف البوت للمجموعه وقم بالرد ع الشخص بكلمة همسه 🧸🎁**\n\n𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 -** @ZedThon"
        ics_c += f"**- قم بنسخ :**\n `@zzll_bot الرساله ثم معرف الشخص`"
        await lon.client.send_file(lon.chat_id, WPIC, caption=ics_c, reply_to=ld)

