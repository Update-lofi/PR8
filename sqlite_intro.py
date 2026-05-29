import sqlite3

# Подключаемся к базе данных (файл mybase.db)
# Если файла нет, он создастся автоматически
conn = sqlite3.connect('mybase.db')

# Создаём курсор — объект для выполнения запросов
cursor = conn.cursor()

print("База данных создана и подключена!")

# Создаём таблицу users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

# Сохраняем изменения
conn.commit()

print("Таблица users создана!")

# Добавляем одного пользователя
cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''', ('Анна', 25))

# Добавляем нескольких пользователей
users = [
    ('Иван', 30),
    ('Мария', 22),
    ('Петр', 35)
]
cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', users)

conn.commit()
print("Пользователи добавлены!")