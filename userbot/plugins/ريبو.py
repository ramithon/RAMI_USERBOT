from userbot.Config import Config
from userbot import bot 

O = Config.OWNER_ID
Name = bot.me.first_name
M = f"[{Name}](tg://user?id={O})"

A = "https://dashboard.heroku.com/new?template=https://github.com/Zedthon/zedpack/"

B = "**⌔∮ اهلا عزيزي - {} \n⌔∮ رابط التنصيب - [اضغط هنا]({})**"

@icssbot.on(icss_cmd(pattern="رابط التنصيب"))
async def _(e):
    await eor(e, B.format(M, A))
