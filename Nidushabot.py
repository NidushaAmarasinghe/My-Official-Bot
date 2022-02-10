import os
import telebot


bot = telebot.TeleBot("5051018178:AAFvQLshsVonGCofnew9bQsQvMhb-VfkIEE")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hey There! This Is @NidushaAmarasinghe's Official Bot\nJoin:-@SlapTap")
   reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕", url=f"https://t.me/NidushaOfficial_Bot?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "❔About❔", callback_data="cbhowtouse")
                ],[
                    
                    InlineKeyboardButton(
                        "💝 Donate", url=f"https://t.me/NidushaAmarasinghe")
                ],[
                    InlineKeyboardButton(
                        "🧑‍💻Support Group🧑‍💻", url=f"https://t.me/SlapTaps"
                    ),
                    InlineKeyboardButton(
                        "🔁Update Channel🔁", url=f"https://t.me/SlapTaps")
                ],[
                    InlineKeyboardButton(
                        "🛠️Source Code🛠️", url="https://github.com/NidushaAmarasinghe/My-Official-Bot"
                    )
                ]
            ]
        ),


@bot.message_handler(commands=["help"])
def send_message(message):
  bot.send_message(message.chat.id, "Do You Want Help❔")
  reply_markup=InlineKeyboardMarkup(
            [
                [
                  InlineKeyboardButton(
                        "🧑‍💻Support Group🧑‍💻", url=f"https://t.me/SlapTaps"
                    ),
                    InlineKeyboardButton(
                        "🔁Support Channel🔁", url=f"https://t.me/SlapTap"
                    )
                ]
            ]
        ),
    )

@bot.message_handler(commands=["alive"])
def send_welcome(message):
  bot.reply_to(message, "Hey There! Bot Online now. 💃🏻♥️\n**Developer:** @NidushaAmarasinghe\n**Official Website:www.nidushaofficial.tk**\nThank You For Using **Nidusha Official Bot**")
  reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton(
                        "🧑‍💻Support Group🧑‍💻", url=f"https://t.me/SlapTaps"
                    ),
                    InlineKeyboardButton(
                        "🔁Support Channel🔁", url=f"https://t.me/SlapTap"
                    )
                ]
            ]
        )
    )

reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton(
                        "🧑‍💻Support Group🧑‍💻", url=f"https://t.me/SlapTaps"
                    ),
                    InlineKeyboardButton(
                        "🔁Support Channel🔁", url=f"https://t.me/SlapTap"
                    )
                ]
            ]
        )
    )
@bot.message_handler(commands=["about"])
def send_welcome(message):
  bot.reply_to(message, "Hey There! This Is @NidushaAmarasinghe's Official Bot\nJoin:-@SlapTap")
  reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton(
                        "🧑‍💻Support Group🧑‍💻", url=f"https://t.me/SlapTaps"
                    ),
                    InlineKeyboardButton(
                        "🔁Support Channel🔁", url=f"https://t.me/SlapTap"
                    )
                ]
            ]
        )
    )


@bot.message_handler(content_types=["photo", "sticker"])
def send_content_message(msg):
    bot.reply_to(msg, "That's not a text message!")


bot.polling()
