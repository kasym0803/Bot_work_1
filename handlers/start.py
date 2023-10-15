import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from keyboards.inline_buttons import (
    start_keyboard,
    admin_keyboard,
)


async def start_but(massage: types.Message):
    print(massage)
    # try:
    Database().sql_insert_user_query(
            telegram_id=massage.from_user.id,
            username=massage.from_user.username,
            first_name=massage.from_user.first_name,
            last_name=massage.from_user.last_name,
        )
    # except sqlite3.IntegrityError:
    #     pass
    # await bot.send_message(
    #     chat_id=massage.chat.id,
    #     text=f"Hello im your first bot, your id:{massage.from_user.id}",
    #     reply_markup=await start_keyboard()
    # )
    # with open("/Users/User/.vscode/Bot_34-1_work1/media/bot_photo_1.jpg", 'rb') as photo:
    #     await bot.send_photo(
    #         chat_id=massage.chat.id,
    #         photo=photo,
    #         caption=f"Hello im your first bot \n your id:{massage.from_user.id}",
    #         reply_markup=await start_keyboard()
    #     )
    with open("/Users/User/.vscode/Bot_34-1_work1/media/bot_gif.gif", 'rb') as animation:
        await bot.send_animation(
            chat_id=massage.chat.id,
            animation=animation,
            caption=f"Hello im your first bot \n your id:{massage.from_user.id}",
            reply_markup=await start_keyboard()
        )


async def ban_word(message: types.Message):
    if message.from_user.id == 3571983145:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Long time no see, Admin!",
            reply_markup=await admin_keyboard()
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="You have no rights"
        )


async def admin_user_list_call(call: types.CallbackQuery):
    users = Database().sql_select_all_user_query()
    user_list = []
    for user in users:
        if user['username']:
            user_list.append(user["username"])
        else:
            user_list.append(user["first_name"])
    await bot.send_message(
        chat_id=call.from_user.id,
        text="\n".join(user_list)
    )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_but, commands=["start"])
    dp.register_message_handler(ban_word, lambda word: "dorei" in word.text)
    dp.register_callback_query_handler(admin_user_list_call,
                                       lambda word: word.data == "admin_user_list")
