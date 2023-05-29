# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# scheduler = AsyncIOScheduler()
# config.py

from config import bot, #scheduler
from aiogram.types import Message

# from config import scheduler
# from handlers.notiflication import handle_scheduler
# scheduler.start()
# dp.register_message_handler(handle_scheduler, commands=['sche'])
# main.py

async def handle_scheduler(message:Message):
    scheduler.add_job(
        send_notiflication,
        'cron',
        day_of_week='last mon',
        hour='22',
        args=(message.from_user.id, )
    )
    await message.answer('хорошо напомню')

async def send_notiflication(chat_id:int):
    await bot.send_message(chat_id=chat_id, text='напоминаюю')

