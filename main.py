import telebot, requests, json
from telebot import types
from os import getenv

# Markup
mark1 = telebot.types.InlineKeyboardMarkup()
mark1.add(telebot.types.InlineKeyboardButton(text='🔁Updates🔁', url='https://t.me/SlapTap'),
          telebot.types.InlineKeyboardButton(text='🧑‍💻Support🧑‍💻', url='https://t.me/SlapTaps')),
mark1.add(telebot.types.InlineKeyboardButton(text='➕Add To Group➕', url="https://t.me/NidushaOfficial_Bot?startgroup=true")),

mark2 = telebot.types.InlineKeyboardMarkup()
mark2.add(telebot.types.InlineKeyboardButton(text='🔁Updates🔁', url='https://t.me/SlapTap'),
          telebot.types.InlineKeyboardButton(text='🧑‍💻Support🧑‍💻', url='https://t.me/SlapTaps')),
mark2.add(telebot.types.InlineKeyboardButton(text='🛠️Developer🛠️', url="https://t.me/NidushaAmarasinghe")),

mark3 = telebot.types.InlineKeyboardMarkup()
mark3.add(telebot.types.InlineKeyboardButton(text='🔁Updates🔁', url='https://t.me/SlapTap'),
          telebot.types.InlineKeyboardButton(text='🧑‍💻Support🧑‍💻', url='https://t.me/SlapTaps')),
mark3.add(telebot.types.inlinekeyboardButton('❔About❔',query.answer("Hi ",show_alert=true)),

@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "**Hey There! This Is @NidushaAmarasinghe's Official Bot\nJoin:-@SlapTap**",parse_mode='Markdown', reply_markup=mark1)
   
@bot.message_handler(commands=["help"])
def send_message(message):
  bot.send_message(message.chat.id, "Do You Want Help❔",parse_mode='Markdown', reply_markup=mark2)
 
@bot.message_handler(commands=["alive"])
def send_welcome(message):
  bot.reply_to(message, "Hey There! Bot Online now. 💃🏻♥️\nDeveloper:-@NidushaAmarasinghe\nOfficial Website:-www.nidushaofficial.tk\nThank You For Using Nidusha Official Bot")
 
@bot.message_handler(commands=["about"])
def send_welcome(message):
  bot.reply_to(message, "📕 ᴀʙᴏᴜᴛ ᴍᴇ\n\n○ ᴍʏ ɴᴀᴍᴇ : Nidusha Official ʙᴏᴛ⚡️ (http://t.me/NidushaOfficial_Bot)\n○ ʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ\n○ ғʀᴀᴍᴇᴡᴏʀᴋ: ᴘʏʀᴏɢʀᴀᴍ (https://docs.pyrogram.org/)\n○ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ :🔐/n○ ᴠᴇʀsɪᴏɴ : 5.1\n○ ᴄʀᴇᴀᴛᴏʀ : @NidushaAmarasinghe\nJoin:-@SlapTap",parse_mode='Markdown', reply_markup=mark3)

@bot.message_handler(commands=["pic"])
def send_welcome(message):
  await bot.reply_photo(
       chat_id=message.chat.id,
       photo='',
       caption='hii'
  
@bot.message_handler(content_types=["photo", "sticker"])
def send_content_message(message):
    bot.send_photo(message.chat.id, "https://telegra.ph/file/87297d011cb91b4ec3014.jpg")
    

    


bot.polling()
