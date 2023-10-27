from aiogram import types, Dispatcher
from config import bot
from aiogram.utils.deep_linking import _create_link
import binascii
import os
from database.sql_commands import Database
from keyboards.inline_buttons import (
    questionnaire_one_keyboard,
    reference_button
)


async def reference_menu_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"Привет {call.from_user.first_name}\nreference menu",
        reply_markup=await reference_button()
    )


async def reference_link_call(call: types.CallbackQuery):
    user = Database().sql_select_user_form_query(
        telegram_id=call.from_user.id,

    )
    print(user)
    if not user[0]["link"]:
        token = binascii.hexlify(os.urandom(8)).decode()
        link = await _create_link(link_type="start", payload=token)
        print(link)
        Database().sql_update_reference_link_query(
            link=link,
            telegram_id=call.from_user.id
        )
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Привет {call.from_user.first_name}\n"
                f"Here is your new link {link}",
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Привет {call.from_user.first_name}\n"
                f"Here is your new link {user[0]['link']},"
        )

async def referal_list_call(call: types.CallbackQuery):
    referal_user = Database().sql_select_referal_by_owner_query(
        owner=call.from_user.id,
    )
    data = []
    if referal_user:
        for user in referal_user:
            data.append(f"[{user['referal']}](tg://user?id={user['referal']})")
        text = '\n'.join(data)
        await bot.send_message(
            chat_id=call.from_user.id,
            text=text,
            parse_mode=types.ParseMode.MARKDOWN
        )

def register_reference_menu_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(reference_menu_call,
                                       lambda call: call.data == "referall")
    dp.register_callback_query_handler(reference_link_call,
                                       lambda call: call.data == "reference_link")
    dp.register_callback_query_handler(referal_list_call,
                                       lambda call: call.data == "reference_list")
