import sqlite3

connection = sqlite3.connect('not_telegram2.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

for i in range(10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)", (f'User{i+1}', f'example{i+1}@gmail.com', i*10+10, 1000))

cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")

cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

cursor.execute("SELECT * FROM Users WHERE age != 60")
users = cursor.fetchall()

for user in users:
    username, email, age, balance = user[1], user[2], user[3], user[4]
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
all_balance = cursor.fetchone()[0]

print(all_balance/total_users)


connection.commit()
connection.close()
