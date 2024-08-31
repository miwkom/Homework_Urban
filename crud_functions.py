import sqlite3

connection = sqlite3.connect('../not_telegram3.db')
cursor = connection.cursor()


def initiate_db():
    connection = sqlite3.connect('../not_telegram3.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Product(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('../not_telegram3.db')
    cursor = connection.cursor()
    cursor.execute("SELECT title, description, price FROM PRODUCT")
    return cursor.fetchall(), connection.close()


# for i in range(4):
#     cursor.execute('INSERT INTO Product (title, description, price) VALUES (?,?,?)',
#                    (f'Продукт{i + 1}', f'Описание{i + 1}', f'{i + 1}00'))

connection.commit()
connection.close()
