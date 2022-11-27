import sqlite3
import db
import cgi
from lxml import etree
connect = sqlite3.connect('painting.db')
cursor = connect.cursor()
sql = cursor.execute('''SELECT picture_id, Pictures.name, genre, year, Painters.name, Galleries.name FROM Pictures
                    JOIN Painters ON Pictures.painter_id = Painters.painter_id
                    JOIN Galleries ON Pictures.gallery_id = Galleries.gallery_id''')
print('Content-type:text/html\n')
print('''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Таблица Pictures</title>
    </head>
    <body>
        <table border="3" align="center" width="70%" cellspacing="0">
            <tr>
        <th>№</th>
        <th>Название картины</th>
        <th>Жанр</th>
        <th>Год</th>
        <th>Художник</th>
        <th>Название галереи</th>
            <tr>
    ''')
for s in sql:
    print('<td>{}</td>'.format(s[0]))
    print('<td>{}</td>'.format(s[1]))
    print('<td>{}</td>'.format(s[2]))
    print('<td>{}</td>'.format(s[3]))
    print('<td>{}</td>'.format(s[4]))
    print('<td>{}</td>'.format(s[5]))
    print('<tr>')
print('''</table>
    </body>
    </html>''')