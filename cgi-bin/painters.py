#!/usr/bin/env python3
import cgi
import html
import sqlite3
import db

form = cgi.FieldStorage()
name = form.getfirst('name')#читаем данные, введенные пользователем в поле name
country = form.getfirst('country')#читаем данные, введенные пользователем в поле country
name = html.escape(name)
country = html.escape(country)


con = sqlite3.connect('painting.db')
cur = con.cursor()

try:
    db.add_painter(name, country)
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
