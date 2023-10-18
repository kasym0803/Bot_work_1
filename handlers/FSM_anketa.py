from config import bot, dp
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from database.sql_commands import Database


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
    photo = await message.photo[-1].download(destination='C:/Users/User/.vscode/Bot_34-1_work1/media')
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
        await message.answer('Вы были добавленны в базу данных')
    elif message.text.lower() == "нет":
        await message.answer('Отменено')
        await state.finish()
    else:
        await message.answer('Пишите да или  нет')


def register_fsm_handlers(dp: Dispatcher):
    dp.register_message_handler(start_fsm, commands=['anceta'])
    dp.register_message_handler(load_username, state=Anceta.username, content_types=['text'])
    dp.register_message_handler(load_bio, state=Anceta.bio, content_types=['text'])
    dp.register_message_handler(load_photo, state=Anceta.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=Anceta.submit, content_types=['text'])
