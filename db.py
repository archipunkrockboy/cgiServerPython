import sqlite3


def create_tables(con, cur):
    cur.execute('CREATE TABLE IF NOT EXISTS Painters'
                '(painter_id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'name TEXT, '
                'country TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS Galleries'
                '(gallery_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'name TEXT, '
                'city TEXT, '
                'country TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS Pictures'
                '(picture_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'gallery_id INTEGER, '
                'painter_id INTEGER, '
                'name TEXT, '
                'genre TEXT, '
                'year DATE,'
                'FOREIGN KEY (gallery_id) REFERENCES Galleries(gallery_id), '
                'FOREIGN KEY (painter_id) REFERENCES Painters(painter_id))'
                )
    con.commit()


def make_commit(sql, data):
    cur = connect.cursor()
    cur.execute(sql, data)
    connect.commit()


def add_painter(name, country):
    sql = 'INSERT INTO Painters(name, country) VALUES (?, ?)'
    make_commit(sql, (name, country))


def add_gallery(name, city, country):
    sql = 'INSERT INTO Galleries(name, city, country) VALUES (?, ?, ?)'
    make_commit(sql, (name, city, country))


def add_picture(gallery_id, painter_id, name, genre, year):
    sql = 'INSERT INTO Pictures(gallery_id, painter_id, name, genre, year) VALUES (?, ?, ?, ?, ?)'
    make_commit(sql, (gallery_id, painter_id, name, genre, year))


def print_pictures():
    cursor.execute('''SELECT Pictures.name, genre, year, Painters.name, Galleries.name FROM Pictures
                    JOIN Painters ON Pictures.painter_id = Painters.painter_id
                    JOIN Galleries ON Pictures.gallery_id = Galleries.gallery_id''')
    print(cursor.fetchall())


def get_galleries():
    cursor.execute('''SELECT * FROM Galleries''')
    return cursor.fetchall()


def print_galleries():
    cursor.execute('SELECT name, city, country FROM Galleries')
    print(cursor.fetchall())


def print_painters():
    cursor.execute('SELECT name, country FROM Painters')
    print(cursor.fetchall())


connect = sqlite3.connect('painting.db')  # создаём или подключаемся к БД painting
cursor = connect.cursor()  # создаём курсор для выполнения инструкций SQL

