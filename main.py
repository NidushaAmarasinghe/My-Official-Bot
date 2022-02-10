import telebot, requests, json
from telebot import types
from os import getenv

bot = telebot.TeleBot(getenv("BOT_TOKEN"))


# Markup
mark1 = telebot.types.InlineKeyboardMarkup()
mark1.add(telebot.types.InlineKeyboardButton(text='🔁Updates🔁', url='https://t.me/SlapTap'),
          telebot.types.InlineKeyboardButton(text='🧑‍💻Support🧑‍💻', url='https://t.me/SlapTaps')),
mark1.add(telebot.types.InlineKeyboardButton(text='➕Add To Group➕', url="https://t.me/NidushaOfficial_Bot?startgroup=true")),


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "<b>Hey There! This Is @NidushaAmarasinghe's Official Bot</b>\nJoin:-@SlapTap",parse_mode='Markdown', reply_markup=mark1)
   
@bot.message_handler(commands=["help"])
def send_message(message):
  bot.send_message(message.chat.id, "Do You Want Help❔")
 
@bot.message_handler(commands=["alive"])
def send_welcome(message):
  bot.reply_to(message, "Hey There! Bot Online now. 💃🏻♥️\n**Developer:** @NidushaAmarasinghe\n**Official Website:www.nidushaofficial.tk**\nThank You For Using **Nidusha Official Bot**")
 
@bot.message_handler(commands=["about"])
def send_welcome(message):
  bot.reply_to(message, "Hey There! This Is @NidushaAmarasinghe's Official Bot\nJoin:-@SlapTap")
  
@bot.message_handler(content_types=["photo", "sticker"])
def send_content_message(msg):
    bot.reply_to(msg, "That's not a text message!")
    

    


bot.polling()
