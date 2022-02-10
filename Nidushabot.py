
import logging
from time import time
from datetime import datetime
from NidushaOfficial_Bot.config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, SUPPORT_GROUP
from NidushaOfficial_Bot.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from NidushaOfficial_Bot.helpers.decorators import sudo_users_only

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""✨ Welcome {message.from_user.first_name} \n
💭This Is Nidusha Amarasinghe's Official Bot\n**Developer :- @NidushaAmarasinghe**""",
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
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅Hey There! Nidusha Official Bot Is Running😘 **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ Group", url=f"https://t.me/SlapTaps"
                    ),
                    InlineKeyboardButton(
                        "📣 Channel", url=f"https://t.me/SlapTap"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""Do You Want Help❔""",
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

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""Do You Want Help❔""",
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


@Client.on_message(command(["about", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "Hey There! This Is @NidushaAmarasinghe's Official Bot\n"
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

@Client.on_message(command(["alive", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "Hey There! Bot Online now. 💃🏻♥️\n**Developer:** @NidushaAmarasinghe\n**Official Website:https://amdaniwasa.com**\nThank You For Using **Nidusha Official Bot**"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
