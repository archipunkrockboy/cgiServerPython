import sqlite3
import db
import cgi

connect = sqlite3.connect('painting.db')
cursor = connect.cursor()
sql = cursor.execute('SELECT * FROM Galleries')
print('Content-type:text/html\n')
print('''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Таблица Galleries</title>
    </head>
    <body>
        <table border="3" align="center" width="70%" cellspacing="0">
            <tr>
        <th>№</th>
        <th>Название галереи</th>
        <th>Город</th>
        <th>Страна</th>
            <tr>
    ''')
for s in sql:
    print('<td>{}</td>'.format(s[0]))
    print('<td>{}</td>'.format(s[1]))
    print('<td>{}</td>'.format(s[2]))
    print('<td>{}</td>'.format(s[3]))
    print('<tr>')
print('''</table>
    <br>
    <label>Загрузить данные из файла</label>
    <form action="/cgi-bin/download_from_xml.py" method="post" enctype="multipart/form-data">
    <input class="form-control" name="xml_file" type="file" accept=".xml">
    <input type="submit" name="xml_file1">
    </form>
    <br>
    <a class="link-primary" target="_blank" download="galleries.xml" href="/cgi-bin/get_galleries_xml.py">Выгрузить в .xml</a>
    <br>
    </body>
    </html>''')