from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

eat_button = KeyboardButton('/eat')
start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2,
).add(eat_button)

order_button = KeyboardButton('Заказать')
cancle_button = KeyboardButton('Отменить заказ')

yes = KeyboardButton('да')
no = KeyboardButton('нет')
yes_no_markup = ReplyKeyboardMarkup(
    row_width=2,
    one_time_keyboard=True,
    resize_keyboard=True,
).add(yes, no)

