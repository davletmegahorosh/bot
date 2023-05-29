from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from keyboards import client_kb
from database.database import sql_command_create

class FSMadmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    photo = State()
    submit = State()
async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMadmin.name.set()
        await message.answer('Что хотите заказать?', reply_markup=client_kb.start_markup)
    else:
        await message.answer('в группах не работает !!! Мой хозяин умный!!!')

async def fsm_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f'@{message.from_user.username}'
        data['name'] = message.text
    await message.answer('сколько лет?')
    await FSMadmin.next()

async def fsm_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('только числа')
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMadmin.next()
        await message.answer('какого пола?', reply_markup=client_kb.start_markup)

async def fsm_gender(message: types.Message, state: FSMContext):
    if message.text not in ['мужчина','женщина','не знаю']:
        await message.answer('выбери из списка')
    else:
        async with state.proxy() as data:
            data['gender'] = message.text
        await FSMadmin.next()
        await message.answer('Че там?')

async def fsm_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        await message.answer_photo(f"{data['photo']}", caption=f"{data['name']}\n {data['age']}\n {data['gender']}\n {data['username']}")
    await FSMadmin.next()
    await message.answer('Всё правильно?', reply_markup=client_kb.submit_markup)

async def fsm_submit(message: types.Message, state: FSMContext):
    if message.text == 'да':
        await sql_command_create(state)
        await state.finish()
        await message.answer('заказ отрпавлен админу', reply_markup=client_kb.start_markup)
    elif message.text  == 'нет':
        await state.finish()
        await message.answer('Заказ отменён', reply_markup=client_kb.start_markup)
    else:
        await message.answer('выберите ответ да или нет', reply_markup=client_kb.submit_markup)

async def fsm_cancle(message: types.Message, state: FSMContext):
    cur_state = await state.get_state()
    if cur_state is not None:
        await state.finish()
        await message.answer('Заказ отменён')

def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(fsm_cancle, state="*", commands=['cancle'])
    dp.register_message_handler(fsm_cancle, Text(equals='cancle', ignore_case= True), state="*")

    dp.register_message_handler(fsm_start, commands=['eat'])
    dp.register_message_handler(fsm_name, state=FSMadmin.name)
    dp.register_message_handler(fsm_age, state=FSMadmin.age)
    dp.register_message_handler(fsm_gender, state=FSMadmin.gender)
    dp.register_message_handler(fsm_photo, state=FSMadmin.photo, content_types=['photo'])
    dp.register_message_handler(fsm_submit, state=FSMadmin.submit)

