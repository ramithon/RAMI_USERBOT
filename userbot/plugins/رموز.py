#ZedThon

import asyncio
import random

Ulodya = [
   "𓄂",
   "⇲",
   "𖦼",
   "❒", 
   "༕",
   "༗",
   "",
   "༗",
   "⌭",
]

@icssbot.on(
    icss_cmd(
       pattern="رموز", outgoing=True
    )
)
async def icss(ics):
   Ulo = random.choics(Ulodya)
   await icss.edit("**وجع انتظر...**")
   await asyncio.sleep(3)
   await eor(ics, Ulo)
