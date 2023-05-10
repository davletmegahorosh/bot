from aiogram import types, Dispatcher
from .fsm_func import intro
from keyboards.client_kb import start_markup

photo = open('media/papa.jpg', 'rb')


async def start(message: types.Message):
    await message.answer_photo(photo = photo, caption=intro,
                           reply_markup=start_markup)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start,commands=['start'])



