import re

from config import bot, dp
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.inline_buttons import like_dislike_keyboard

from database.sql_commands import Database
import random


class Anceta(StatesGroup):
    username = State()
    bio = State()
    photo = State()
    submit = State()


async def start_fsm(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Напишите ваше имя')
    await Anceta.username.set()


async def load_username(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await Anceta.next()
    await message.answer('Пропишите ваш биографию')


async def load_bio(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
    await Anceta.next()
    await message.answer('Отправьте фотографию!')


async def load_photo(message: types.Message, state: FSMContext):
    photo = await message.photo[-1].download(destination_dir='C:/Users/User/.vscode/Bot_34-1_work1/media')
    async with state.proxy() as data:
        data['photo'] = photo.name
    photo_path = data["photo"]
    with open(photo_path, 'rb') as photos:
        await message.answer_photo(photos, caption=f'Имя: {data["username"]}\nБиография: {data["bio"]}')
        await message.answer('Правильно?')
    await Anceta.next()


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        async with state.proxy() as data:
            Database().sql_insert_anketa_users(telegram_id=message.from_user.id,
                                               username=data['username'],
                                               bio=data['bio'],
                                               photo=data['photo'])
            print(data)
            await message.answer('Вы были добавленны в базу данных')
            await state.finish()
    elif message.text.lower() == "нет":
        await message.answer('Отменено')
        await state.finish()
    else:
        await message.answer('Пишите да или  нет')


async def random_profiles_call(call: types.CallbackQuery):
    users = Database().sql_select_all_user_form_query()
    random_choise = random.choice(users)
    print(random_choise)
    photoss = random_choise[4]
    with open(photoss, 'rb') as photo:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=f"Nickname: {random_choise[2]}\n"
                    f"Bio: {random_choise[3]}\n",
            reply_markup=await like_dislike_keyboard(),
        )


def register_fsm_handlers(dp: Dispatcher):
    dp.register_message_handler(start_fsm, commands=['anceta'])
    dp.register_message_handler(load_username, state=Anceta.username, content_types=['text'])
    dp.register_message_handler(load_bio, state=Anceta.bio, content_types=['text'])
    dp.register_message_handler(load_photo, state=Anceta.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=Anceta.submit, content_types=['text'])
    dp.register_callback_query_handler(random_profiles_call, lambda call: call.data == 'random_profiles'
                                                                          or call.data == f'user_form_like'
                                                                          or call.data == f'user_form_dislike')
