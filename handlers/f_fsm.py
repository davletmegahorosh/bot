from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from keyboards import client_kb, food_markups
from handlers import fsm_func

class FSM(StatesGroup):
        menu = State()
        pizza = State()
        combo = State()
        zakuski = State()
        desserts = State()
        drinks = State()
        salat = State()
        souse = State()
        extra = State()
        submit = State()

async def fsm_start(message: types.Message, state: FSMContext):
    if message.chat.type == 'private':
        await FSM.menu.set()
        await message.answer('Добавляйте в корзину всё что вам нужно',
                             reply_markup=food_markups.menu_markup)
    else:
        await message.answer('В группах не работает')

async def pizza_catalog(message: types.Message, state: FSMContext):
    await FSM.pizza.set()
    for i in fsm_func.pizza:
        await message.answer(
            f"{i['photo']}\n"
            f"название:\n  {i['title']}\n"
            f"цена:\n {i['price']}\n"
            f"ингредиенты:\n  {i['ingredients']}\n")
    await bot.send_message(message.from_user.id, 'Для выбора других видов еды нажмите на кнопки',
                           reply_markup=food_markups.pizza_markup)

async def combo_catalog(message: types.Message, state: FSMContext):
    await FSM.combo.set()
    for i in fsm_func.combo:
        await message.answer(
            f"{i['photo']}\n"
            f"название:\n  {i['title']}\n"
            f"цена:\n {i['price']}\n"
            f"ингредиенты:\n  {i['ingredients']}\n")
    await bot.send_message(message.from_user.id, 'Для выбора других видов еды нажмите на кнопки',
                           reply_markup=food_markups.pizza_markup)

async def zakuski_catalog(message: types.Message, state: FSMContext):
    await FSM.zakuski.set()
    for i in fsm_func.zakuski:
        await message.answer(
            f"{i['photo']}\n"
            f"название:\n  {i['title']}\n"
            f"цена:\n {i['price']}\n"
            f"ингредиенты:\n  {i['ingredients']}\n")
    await bot.send_message(message.from_user.id, 'Для выбора других видов еды нажмите на кнопки',
                           reply_markup=food_markups.pizza_markup)

async def dessert_catalog(message: types.Message, state: FSMContext):
    await FSM.desserts.set()
    for i in fsm_func.dessert:
        await message.answer(
            f"{i['photo']}\n"
            f"название:\n  {i['title']}\n"
            f"цена:\n {i['price']}\n"
            f"ингредиенты:\n  {i['ingredients']}\n")
    await bot.send_message(message.from_user.id, 'Для выбора других видов еды нажмите на кнопки',
                           reply_markup=food_markups.pizza_markup)

async def drinks_catalog(message: types.Message, state: FSMContext):
    await FSM.drinks.set()
    for i in fsm_func.drinks:
        await message.answer(
            f"{i['photo']}\n"
            f"название:\n  {i['title']}\n"
            f"цена:\n {i['price']}\n"
            f"ингредиенты:\n  {i['ingredients']}\n")
    await bot.send_message(message.from_user.id, 'Для выбора других видов еды нажмите на кнопки',
                           reply_markup=food_markups.pizza_markup)

async def salat_catalog(message: types.Message, state: FSMContext):
    await FSM.salat.set()
    for i in fsm_func.salat:
        await message.answer(
            f"{i['photo']}\n"
            f"название:\n  {i['title']}\n"
            f"цена:\n {i['price']}\n"
            f"ингредиенты:\n  {i['ingredients']}\n")
    await bot.send_message(message.from_user.id, 'Для выбора других видов еды нажмите на кнопки',
                           reply_markup=food_markups.pizza_markup)

async def souse_catalog(message: types.Message, state: FSMContext):
    await FSM.souse.set()
    for i in fsm_func.souse:
        await message.answer(
            f"{i['photo']}\n"
            f"название:\n  {i['title']}\n"
            f"цена:\n {i['price']}\n"
            f"ингредиенты:\n  {i['ingredients']}\n")
    await bot.send_message(message.from_user.id, 'Для выбора других видов еды нажмите на кнопки',
                           reply_markup=food_markups.pizza_markup)

async def extra_catalog(message: types.Message, state: FSMContext):
    await FSM.extra.set()
    for i in fsm_func.extra:
        await message.answer(
            f"{i['photo']}\n"
            f"название:\n  {i['title']}\n"
            f"цена:\n {i['price']}\n"
            f"ингредиенты:\n  {i['ingredients']}\n")
    await bot.send_message(message.from_user.id, 'Для выбора других видов еды нажмите на кнопки',
                           reply_markup=food_markups.pizza_markup)

async def fill_list(message: types.Message, state: FSMContext):
    if not message.reply_to_message:
        await message.answer('Отпправьте сообщение как ответ к тому продукту который вы хотите добавить в корзину')
    else:
        async with state.proxy() as data:
            data[f'{message.from_user.id,message.reply_to_message.message_id}'] = message.reply_to_message.text
        await message.answer('Успешно добавлено в корзину')

async def fsm_submit1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        for j in data.values():
            if not str(j).isdigit():
                await message.answer(j)
    await message.answer('Все правильно?', reply_markup=client_kb.yes_no_markup)
    await FSM.submit.set()

async def fsm_submit2(message: types.Message, state: FSMContext):
    if message.text == 'да':
        await message.forward(1154757842)
        async with state.proxy() as data:
            for i in data.values():
                if not str(i).isdigit():
                    await bot.send_message(1154757842, i)
        await state.finish()
        await message.answer('Ваш заказ отрпавлен оператору. Пожалуста ожидайте ответа', reply_markup=client_kb.start_markup)
    elif message.text  == 'нет':
        await state.finish()
        await message.answer('Заказ отменён', reply_markup=client_kb.start_markup)
    else:
        await message.answer('Выберите ответ да или нет', reply_markup=client_kb.yes_no_markup)

async def fsm_cancle(message: types.Message, state: FSMContext):
    cur_state = await state.get_state()
    if cur_state is not None:
        # async with state.proxy() as data:
            # for i in range(data[f'{message.from_user.id}id'], message.message_id):
            #     await bot.delete_message(message.from_user.id, i)
        await state.finish()
        await message.answer('Заказ отменён', reply_markup=client_kb.start_markup)

def register_papa_handlers(dp: Dispatcher):
    dp.register_message_handler(fsm_cancle, Text(equals='Отменить заказ', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['eat'])
    dp.register_message_handler(fill_list, Text(equals='+'), state="*")
    dp.register_message_handler(pizza_catalog, Text(equals='Пицца'), state="*")
    dp.register_message_handler(combo_catalog,  Text(equals='Комбо'), state="*")
    dp.register_message_handler(zakuski_catalog,  Text(equals='Закуски'), state="*")
    dp.register_message_handler(dessert_catalog,  Text(equals='Десерты'), state="*")
    dp.register_message_handler(drinks_catalog,  Text(equals='Напитки'), state="*")
    dp.register_message_handler(salat_catalog,  Text(equals='Салаты'), state="*")
    dp.register_message_handler(souse_catalog,  Text(equals='Соусы'), state="*")
    dp.register_message_handler(extra_catalog,  Text(equals='доп'), state="*")
    dp.register_message_handler(fsm_submit1,  Text(equals='Заказать'), state="*")
    dp.register_message_handler(fsm_submit2, state=FSM.submit)