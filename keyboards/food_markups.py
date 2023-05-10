from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from .client_kb import cancle_button, order_button

pizza_button = KeyboardButton('Пицца')
combo_button = KeyboardButton('Комбо')
zakuski_button = KeyboardButton('Закуски')
dessert_button = KeyboardButton('Десерты')
drinks_button = KeyboardButton('Напитки')
salat_button = KeyboardButton('Салаты')
souse_button = KeyboardButton('Соусы')
extra_button  = KeyboardButton('доп')

pizza_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                   row_width=2).add(pizza_button,combo_button, zakuski_button,
                                    dessert_button,drinks_button, salat_button, souse_button, extra_button).add(
                                    order_button).add(cancle_button)
menu_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                   row_width=2).add(pizza_button,combo_button, zakuski_button,
                                    dessert_button,drinks_button, salat_button, souse_button, extra_button).add(cancle_button)