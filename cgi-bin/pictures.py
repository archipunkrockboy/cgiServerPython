#!/usr/bin/env python3
import cgi
import html
import sqlite3
import db

form = cgi.FieldStorage()
gallery_id = form.getfirst('gallery_id')
painter_id = form.getfirst('painter_id')
name = form.getfirst('name')#читаем данные, введенные пользователем в поле name
genre = form.getfirst('genre')
year = form.getfirst('year')
# name = html.escape(name)
# country = html.escape(country)


con = sqlite3.connect('painting.db')
cur = con.cursor()

try:
    db.add_picture(gallery_id, painter_id, name, genre, year)
except:
    print('Content-type: text/html\n')
    print('''<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8"
                <title>Добавление данных</title>
            </head>
            <body>''')
    print('<h1>Произошла ошибка!</h1>')
    print(''''</body>
                    </html>''')
else:
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
                <html>
                <head>
                    <meta charset="utf-8">
                    <title>Добавление данных</title>
                </head>
                <body>""")

    print("<h1>Строка добавлена!</h1>")
    print("""</body>
                </html>""")
