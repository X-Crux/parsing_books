# объединение всех book_list файлов в один book_unite

category = [
    'book_lisk_apparatura.csv',
    'book_lisk_avto.csv',
    'book_lisk_belletristika.csv',
    'book_lisk_chelovek.csv',
    'book_lisk_detektivy.csv',
    'book_lisk_dizayn.csv',
    'book_lisk_dizayn-i-grafika.csv',
    'book_lisk_dlya-detey.csv',
    'book_lisk_dom-i-semya.csv',
    'book_lisk_estestvennye-nauki.csv',
    'book_lisk_ezoterika.csv',
    'book_lisk_fantastika.csv',
    'book_lisk_foto-i-video.csv',
    'book_lisk_gumanitarnye-nauki.csv',
    'book_lisk_hobbi-i-razvlecheniya.csv',
    'book_lisk_hobbi-i-remesla.csv',
    'book_lisk_istoriya.csv',
    'book_lisk_kulinariya.csv',
    'book_lisk_kultura.csv',
    'book_lisk_nauchno-populyarnoe.csv',
    'book_lisk_nauka-i-ucheba.csv',
    'book_lisk_os-i-bd.csv',
    'book_lisk_professiya.csv',
    'book_lisk_programmirovanie.csv',
    'book_lisk_proza.csv',
    'book_lisk_psihologiya.csv',
    'book_lisk_raznoe.csv',
    'book_lisk_religiya.csv',
    'book_lisk_romany-erotika.csv',
    'book_lisk_rukodelie.csv',
    'book_lisk_setevye-tehnologii.csv',
    'book_lisk_stihi-i-poeziya.csv',
    'book_lisk_tehnika.csv',
    'book_lisk_uzhasy-mistika.csv',
    'book_lisk_voennaya-istoriya.csv',
    'book_lisk_web-razrabotki.csv',
    'book_lisk_zdorove.csv',
    'book_lisk_zhivopis-i-risovanie.csv',
    'book_lisk_zhurnaly.csv',
]

with open('book_unite.csv', mode='a', encoding='utf8') as file:
    for i in category:
        with open(i, mode='r', encoding='utf8') as file_csv:
            for j in file_csv:
                file.write(j)
