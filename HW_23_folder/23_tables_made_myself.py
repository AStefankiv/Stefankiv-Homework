import sqlite3
import random
from datetime import datetime

db = sqlite3.connect("book_shop23.sqlite")
kursor = db.cursor()

table_users = ("CREATE TABLE IF NOT EXISTS users ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "first_name TEXT,"
               "last_name TEXT,"
               "age INTEGER NOT NULL)")


table_pub_house = ("CREATE TABLE IF NOT EXISTS pub_house ("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "full_name TEXT,"
                   "rating INTEGER DEFAULT 5"
                   ")")

table_books = ("CREATE TABLE IF NOT EXISTS bookss ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "title TEXT,"
               "author TEXT,"
               "year INTEGER NOT NULL,"
               "price INTEGER NOT NULL,"
               "publishing_house_id INTEGER NOT NULL,"
               "FOREIGN KEY (publishing_house_id) REFERENCES pub_house(id))"
               )

table_purchases = ("CREATE TABLE IF NOT EXISTS purchases ("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "user_id INTEGER NOT NULL,"
                   "book_id INTEGER NOT NULL,"
                   "date TEXT DEFAULT CURRENT_TIMESTAMP,"
                   "FOREIGN KEY (user_id) REFERENCES users(id),"
                   "FOREIGN KEY (book_id) REFERENCES books(id))")

kursor.execute(table_users)
kursor.execute(table_pub_house)
kursor.execute(table_books)
kursor.execute(table_purchases)


data_users = [
    ("Oleksiiii", "Klymenok", random.randint(30, 55)),
    ("Elon", "Musk", random.randint(30, 55)),
    ("Test", "Testenko", random.randint(30, 55)),
    ("Ivan", "Mykhailenko", random.randint(30, 55)),
    ("Svitlana", "Bilonozhko", random.randint(30, 55)),
    ("Nobody", "Knows", random.randint(30, 55)),
]

query = "INSERT INTO users (first_name, last_name, age) VALUES (?, ?, ?)"

kursor.executemany(query, data_users)
db.commit()


data_pub_house = [
    ("Ababagalamaga", 5),
    ("Veselka", 4),
    ("Osvita", 5),
]

query = "INSERT INTO pub_house (full_name, rating) VALUES (?, ?)"

kursor.executemany(query, data_pub_house)
db.commit()


data_books = [
    ("Harry Potter", "Rowling", 2001, 500, random.randint(1, 3)),
    ("Harry Potter 2", "Rowling", 2002, 700, random.randint(1, 3)),
    ("Harry Potter 3", "Rowling", 2003, 700, random.randint(1, 3)),
    ("Kobzar", "Shevchenko", 1850, 1000, random.randint(1, 3)),
    ("Lisova Pisnia", "Ukrainka", 1900, 800, random.randint(1, 3)),
    ("Eneida", "Kotliearevskii", 1800, 500, random.randint(1, 3)),
    ("Misto", "Pidmohylnyi", 1950, 900, random.randint(1, 3)),
]

query = "INSERT INTO bookss (title, author, year, price, publishing_house_id) VALUES (?, ?, ?, ?, ?)"

kursor.executemany(query, data_books)
db.commit()


data_purchases = []
for _ in range(16):
    current_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_purchases.append((random.randint(1, 5), random.randint(1, 5), current_data))

query = "INSERT INTO purchases (user_id, book_id, date) VALUES (?, ?, ?)"

kursor.executemany(query, data_purchases)
db.commit()