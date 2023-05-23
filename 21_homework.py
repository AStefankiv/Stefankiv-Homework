## My console code - HW 1, 2, 3
CREATE TABLE "21_homework_console"
(
    id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name TEXT    NOT NULL UNIQUE,
    last_name  TEXT    NOT NULL UNIQUE,
    age        INTEGER NOT NULL
);

INSERT INTO "21_homework_console"(first_name, last_name, age)
VALUES ('Andrew', 'Stefankiv', 31),
       ('Linh', 'Huynh', 24),
       ('Veronika', 'Poluuk', 29),
       ('Vitalii', 'Poluk', 28),
       ('Le', 'Huyn', 22);


## My python file code - HW 1, 2, 3
import sqlite3

connection = sqlite3.connect("db.sqlite")
cursor = connection.cursor()

query = ("CREATE TABLE IF NOT EXISTS homework_21_python ("
         "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
         "first_name TEXT NOT NULL UNIQUE,"
         "last_name TEXT NOT NULL UNIQUE,"
         "age INTEGER NOT NULL)")


cursor.execute(query)

data = [
    ('Andrew', 'Stefankiv', 31),
    ('Linh', 'Huynh', 24),
    ('Veronika', 'Poluuk', 29),
    ('Vitalii', 'Poluk', 28),
    ('Le', 'Huyn', 22),
]

query = "INSERT INTO homework_21_python (first_name, last_name, age) VALUES (?, ?, ?)"

cursor.executemany(query, data)
connection.commit()