from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

TOKEN = '6214520513:AAFhOLPdtxt4apKLhs2hyHyYR8EDWGgz8RI'

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
