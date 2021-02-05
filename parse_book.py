import requests
from bs4 import BeautifulSoup

# парсинг сайта https://basebooks.ru/
# ВНИМАНИЕ! Процесс довольно продолжительный!
# получаем список книг: "название книги|автор\n"
# сохранение в файл .csv. Один файл - одна категория.
# для объединения всех списков книг нужно запустить book_unite.py

categories = {
    'istoriya': 197,
    'belletristika': 92,
    'dlya-detey': 97,
    'zhurnaly': 147,
    'nauchno-populyarnoe': 85,
    'professiya': 18,
    'romany-erotika': 40,
    'hobbi-i-remesla': 197,
    'rukodelie': 242,
    'raznoe': 246,
    'avto': 13,
    'voennaya-istoriya': 39,
    'dizayn': 7,
    'estestvennye-nauki': 81,
    'kulinariya': 151,
    'os-i-bd': 14,
    'psihologiya': 182,
    'stihi-i-poeziya': 7,
    'fantastika': 106,
    'web-razrabotki': 8,
    'apparatura': 147,
    'gumanitarnye-nauki': 148,
    'dizayn-i-grafika': 17,
    'zhivopis-i-risovanie': 23,
    'kultura': 83,
    'uzhasy-mistika': 13,
    'proza': 44,
    'setevye-tehnologii': 11,
    'foto-i-video': 4,
    'chelovek': 44,
    'detektivy': 72,
    'dom-i-semya': 62,
    'zdorove': 174,
    'nauka-i-ucheba': 101,
    'programmirovanie': 89,
    'religiya': 7,
    'tehnika': 58,
    'hobbi-i-razvlecheniya': 16,
    'ezoterika': 54,
}

for category, pages in categories.items():
    file_name = 'book_lisk_' + category + '.csv'
    url_home = 'https://basebooks.ru/' + category + '/'
    url_pages = 'https://basebooks.ru/' + category + '/page/'
    with open(file_name, mode='a', encoding='utf8') as file:
        response = requests.get(url_home)
        soup = BeautifulSoup(response.text, features='html.parser')
        quotes_tit = soup.findAll("div", {"class": "fs_title"})
        quotes_author = soup.findAll("ul", {"class": "fs_ul_info"})

        for i in range(len(quotes_tit)):
            try:
                file.write(quotes_tit[i].a.text + '|')
            except Exception:
                file.write('Неизвестное название книги|')
            try:
                file.write(quotes_author[i].a.text + '\n')
            except Exception:
                file.write('Неизвестный автор\n')

        for i in range(2, pages):
            url = url_pages + str(i) + '/'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, features='html.parser')
            quotes_tit = soup.findAll("div", {"class": "fs_title"})
            quotes_author = soup.findAll("ul", {"class": "fs_ul_info"})

            for j in range(len(quotes_tit)):
                try:
                    file.write(quotes_tit[j].a.text + '|')
                except Exception:
                    file.write('Неизвестное название книги|')
                try:
                    file.write(quotes_author[j].a.text + '\n')
                except Exception:
                    file.write('Неизвестный автор\n')
