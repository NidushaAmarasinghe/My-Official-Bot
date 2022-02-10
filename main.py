import os
import telebot


bot = telebot.TeleBot("5143744746:AAFNtLLvtie6MbvxgT_tbwh1JEviitCLxJY")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hey There! This Is @NidushaAmarasinghe's Official Bot\nJoin:-@SlapTap")
   
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
