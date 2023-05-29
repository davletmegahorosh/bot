import requests
from bs4 import BeautifulSoup

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

URL = 'https://papajohns.kg/bishkek'


def get_html(url):
    req = requests.get(url=url, headers=HEADERS)
    return req


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div',
                          class_="Flipper_Flipper__1iR3F Flipper_Flipper__paper__1OvF7 ProductCard ProductList_ProductList__item__3UmRR")
    products = []
    counter = 0
    for item in items:
        counter += 1
        ingredients = item.find(class_='Subheading_Subheading__1MXqs ProductCard_ProductCard__subheading__2uYmw')
        price = item.find(
            class_='Amount_Amount__1zPkL Amount_Amount__price__dFaAo ProductCard_ProductCard__price__2WUWl Amount_Amount_size_l__1qY9g')
        price_combo = item.find(class_='Amount_Amount__price__dFaAo')
        card = {
            'id': counter,
            'title': item.find('h3').string,
            'ingredients': ingredients.string if ingredients is not None else '',
            'price': price if price is not None else price_combo,
            'photo': item.find(class_='ProductCard_ProductCard__picture__13mT8').find('source').get('srcset')
        }
        products.append(card)
    return products


def get_price(html: list):
    for i in html:
        i['price'] = str(i['price']).replace(
            '<div class="Amount_Amount__1zPkL Amount_Amount__price__dFaAo ProductCard_ProductCard__price__2WUWl Amount_Amount_size_l__1qY9g">',
            '').replace('<!-- --> <span class="Currency_Currency__2gC9M '
                        'Currency_KGS">с</span></div>', '')
    return html


def get_price_combo(html: list):
    for i in html:
        i['price'] = str(i['price']).replace('<div class="Amount_Amount__price__dFaAo">', '').replace('<!-- --> <span '
                                                                                                      'class="Currency_Currency__2gC9M Currency_KGS">с</span></div>',
                                                                                                      '')
    return html


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        products = get_data(html.text)
        c_prod = []
        combo = get_price_combo(products[26:37])
        pizza = get_price(products[:26])
        zakuski = get_price(products[37:53])
        salat = get_price(products[53:55])
        dessert = get_price(products[55:63])
        drinks = get_price(products[63:80])
        souse = get_price(products[80:90])
        extra = get_price(products[90:])
        c_prod.append(pizza)
        c_prod.append(combo)
        c_prod.append(zakuski)
        c_prod.append(salat)
        c_prod.append(dessert)
        c_prod.append(drinks)
        c_prod.append(souse)
        c_prod.append(extra)
        return c_prod
    else:
        raise Exception('bad request')


product_list = parser()