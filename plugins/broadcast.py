from pyrogram import Client ,filters
import os
from helper.database import getid
ADMIN = int(os.environ.get(ADMIN, 5030955924))

@Client.on_message(filters.command(stats) & filters.user(ADMIN))
async def broadcast(_, message)
   users = len(getid())
   await message.reply_text(fTotal User - {users})

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command([broadcast]))
async def broadcast(bot, message)
 if (message.reply_to_message)
   ms = await message.reply_text(Geting All ids from database ...........)
   ids = getid()
   tot = len(ids)
   await ms.edit(fStarting Broadcast .... n Sending Message To {tot} Users)
   for id in ids
     try
     	await message.reply_to_message.copy(id)
     except
     	pass