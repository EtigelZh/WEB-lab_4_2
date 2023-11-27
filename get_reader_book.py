from jinja2 import Template
import sqlite3
from reader_book_model import get_reader, get_book_reader, get_year
# задаем id читателя, для которого формируем страницу
year_pub = 2020
p_name = 'АСТ'
# устанавливаем соединение с базой данных
conn = sqlite3.connect("library.sqlite")
# выбираем записи о том, какие книги брал читатель с параметром reader_id
# столбцы назвать Название, Авторы, Дата_выдачи, Дата_сдачи
df_book_reader = get_book_reader(conn, year_pub, p_name)

# выбираем записи из таблицы reader для формирования поля со списком
df_reader = get_reader(conn)
df_year = get_year(conn)
# закрываем соединение с базой
conn.close()
# открываем файл reader_book_templ.html и читаем шаблон
f_template = open('reader_book_templ.html', 'r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()
# создаем объект-шаблон
template = Template(html)
# генерируем результат на основе шаблона
result_html = template.render(
 year_pub = year_pub,
 combo_box = df_reader,
 combo_box_year = df_year,
 book_reader = df_book_reader,
 len = len,
 table_name = 'book',
 relation = df_book_reader,
 p_name = p_name
 )
#создаем файл для HTML-страницы
f = open('reader_book.html', 'w', encoding ='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
