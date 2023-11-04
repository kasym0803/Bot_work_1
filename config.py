from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


PROXY_URL = 'http://proxy.server:3128'
storage = MemoryStorage()
TOKEN = config('TOKEN')
bot = Bot(token=TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot=bot, storage=storage)
GROUP_ID = [-4041831110, ]
DESTINATION = "C:/Users/User/.vscode/Bot_34-1_work1"
