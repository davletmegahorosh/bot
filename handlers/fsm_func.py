from parser.kfc_parser import product_list

pizza = product_list[0]
combo = product_list[1]
zakuski = product_list[2]
salat = product_list[3]
dessert = product_list[4]
drinks = product_list[5]
souse = product_list[6]
extra = product_list[7]

intro = f"Мне кажется вы проголодались. Самое время подкрепится.\n" \
        f"Закажите еду у Папа джонс Бишек\n\n" \
        f"Для начала нажмите на кнопку /eat" \
        f"Выбирайте виды блюд, что бы добавить блюдо в корзину напишите ответ к блюду '+'" \
        f"после окончания нажмите на заказать или отменить заказ\n" \
