import sqlite3
import db
import cgi

connect = sqlite3.connect('painting.db')
cursor = connect.cursor()
sql = cursor.execute('SELECT * FROM Painters')
print('Content-type:text/html\n')
print('''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Таблица Painters</title>
    </head>
    <body>
        <table border="3" align="center" width="70%" cellspacing="0">
            <tr>
        <th>№</th>
        <th>Художник</th>
        <th>Страна</th>
            <tr>
    ''')
for s in sql:
    print('<td>{}</td>'.format(s[0]))
    print('<td>{}</td>'.format(s[1]))
    print('<td>{}</td>'.format(s[2]))
    print('<tr>')
print('''</table>
    </body>
    </html>''')