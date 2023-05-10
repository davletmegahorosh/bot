from aiogram.utils import executor
import logging
from handlers import client, f_fsm
from config import dp

client.register_handlers_client(dp)
f_fsm.register_papa_handlers(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)