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

share_loc = KeyboardButton('Отправить моё местоположение',request_location=True)
share_con = KeyboardButton('Отправить мой номер', request_contact=True)
start_order = KeyboardButton('Заказать')

share_data = ReplyKeyboardMarkup(row_width=1,
                                 resize_keyboard=True
                                 ).add(share_con, share_loc, start_order)

