import sqlite3

connection = sqlite3.connect('../not_telegram4.db')
cursor = connection.cursor()


def initiate_db():
    connection = sqlite3.connect('../not_telegram4.db')
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


def initiate_db2():
    connection = sqlite3.connect('../not_telegram4.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('../not_telegram4.db')
    cursor = connection.cursor()
    cursor.execute("SELECT title, description, price FROM PRODUCT")
    return cursor.fetchall(), connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('../not_telegram4.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
                   (username, email, age, 1000))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('../not_telegram4.db')
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM Users WHERE username =?", (username,))
    result = cursor.fetchone()[0] > 0
    connection.close()
    return result


if __name__ == '__main__':
    initiate_db()
    initiate_db2()

    add_user('user1', 'user1@example.com', 25)
    print(is_included('user1'))

    # for i in range(4):
    #     cursor.execute('INSERT INTO Product (title, description, price) VALUES (?,?,?)',
    #                    (f'Продукт{i + 1}', f'Описание{i + 1}', f'{i + 1}00'))

connection.commit()
connection.close()
