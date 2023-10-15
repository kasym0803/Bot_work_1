import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database


async def chat_action(message: types.Message):
    ban_word = ["fuck", "bitch", "damn"]
    print(message.chat.id)
    if message.chat.id == -3491649186494:
        for word in ban_word:
            if word in message.text.lower().replace(' ', "",):
                user = Database().sql_select_user_query(
                    telegram_id=message.from_user.id,
                )
                print(user)
                if user:
                    Database().sql_update_ban_user_query(
                        telegram_id=message.from_user.id
                    )
                else:
                    Database().sql_insert_ban_user_query(
                        telegram_id=message.from_user.id,
                        username=message.from_user.username
                    )

                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=message.message_id
                    )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"No curse words in this chat\n"
                         f"Username: {message.from_user.username}"
                    )
    else:
        await message.reply(
            text="There is no such a command\n"
                 "Maybe u mispronounced"
                )

        #  await message.reply(
        #     text=message.text
        #     )


def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(chat_action)

