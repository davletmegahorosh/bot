import requests
from bs4 import BeautifulSoup
# from aiogram import types, Dispatcher
# from parser.shyni_parser import parser
# client

# from handlers import client
# client.register_handlers_client(dp)
# main.py

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

URL = 'https://www.best-tyres.ru/'


def get_html(url):
    req = requests.get(url=url, headers=HEADERS)
    return req


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div',class_="product_item_mobile_inner")
    wheels = []
    for item in items:
        card = {
            'tite' : item.find('h3',itemprop="name").text,
            'price' : item.find('h3',class_="model-min-cost").text.replace('.\n\t\t\t\t\t\t\t\t\t\t\t',''),
            'size' : item.find('div', class_='model-count-goods').text,
            'link' : f"{URL}{item.find('a',class_='product_item_mobile_description').get('href')}"
        }
        wheels.append(card)
    return wheels

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        wheels = []
        cur_pg = get_data(html.text)
        wheels.extend(cur_pg)
        return wheels
    else:
        print('bad reques')

html= get_html(URL)
get_data(html.text)

# async def get_wheels(message: types.Message):
#     wheels = parser()
#     for i in wheels:
#         await message.answer(
#             f"{i['link']}\n\n"
#             f"{i['title']}\n\n"
#             f"{i['price']}\n\n"
#             f"{i['size']}\n\n"
#         )
#
# def register_handlers_client(dp:Dispatcher):
#     dp.register_message_handler(get_wheels, commands=['get'])
# client.py