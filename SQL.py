import sqlite3

connection = sqlite3.connect('Gifts.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Gifts (
ФИО TEXT NOT NULL,
Подарок TEXT NOT NULL,
Стоимость INTEGER NOT NULL,
Статус TEXT
)
''')
cursor.execute('INSERT INTO Gifts (ФИО, Подарок, Стоимость, Статус) VALUES (?, ?, ?, ?)', ('Буток Илья Олегович', 'Кружка', 283, 'Не куплен'))
cursor.execute('INSERT INTO Gifts (ФИО, Подарок, Стоимость, Статус) VALUES (?, ?, ?, ?)', ('Челноков Виталий Владимирович', 'Блокнот', 279, 'Куплен'))
cursor.execute('INSERT INTO Gifts (ФИО, Подарок, Стоимость, Статус) VALUES (?, ?, ?, ?)', ('Уразов Роман Сергеевич', 'Гарнитура', 237, 'Куплен'))
cursor.execute('INSERT INTO Gifts (ФИО, Подарок, Стоимость, Статус) VALUES (?, ?, ?, ?)', ('Кошелев Дмитрий Геннадьевич', 'Эспандер', 233, 'Куплен'))
cursor.execute('INSERT INTO Gifts (ФИО, Подарок, Стоимость, Статус) VALUES (?, ?, ?, ?)', ('Шевчук Никита Андреевич', 'Лампа', 322, 'Не куплен'))
cursor.execute('INSERT INTO Gifts (ФИО, Подарок, Стоимость, Статус) VALUES (?, ?, ?, ?)', ('Максимов Дмитрий Андреевич', 'Фоторамка', 330, 'Куплен'))
cursor.execute('INSERT INTO Gifts (ФИО, Подарок, Стоимость, Статус) VALUES (?, ?, ?, ?)', ('Гарманов Александр Александрович', 'Термос', 347, 'Не куплен'))
cursor.execute('INSERT INTO Gifts (ФИО, Подарок, Стоимость, Статус) VALUES (?, ?, ?, ?)', ('Геллер Сергей Александрович', 'Фоторамка', 332, 'Куплен'))
cursor.execute('INSERT INTO Gifts (ФИО, Подарок, Стоимость, Статус) VALUES (?, ?, ?, ?)', ('Панамарчук Кирилл Эдуардович', 'Гарнитура', 305, 'Не куплен'))
cursor.execute('INSERT INTO Gifts (ФИО, Подарок, Стоимость, Статус) VALUES (?, ?, ?, ?)', ('Боброва Александра Сергеевна', 'Лампа', 294, 'Не куплен'))

cursor.execute('SELECT * FROM Gifts')
users = cursor.fetchall()

for user in users:
  print(user)

connection.commit()
connection.close()