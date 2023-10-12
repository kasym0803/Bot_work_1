import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from keyboards.inline_buttons import start_keyboard


async def start_but(massage: types.Message):
    print(massage)
    try:
        Database().sql_insert_user_query(
            telegram_id=massage.from_user.id,
            username=massage.from_user.username,
            first_name=massage.from_user.first_name,
            last_name=massage.from_user.last_name,
        )
    except sqlite3.IntegrityError:
        pass
    await bot.send_message(
        chat_id=massage.chat.id,
        text=f"Hello im your first bot",
        reply_markup=await start_keyboard()
    )


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_but, commands=["start"])
