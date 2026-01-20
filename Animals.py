import sqlite3

# Підключення до бази даних (створиться автоматично)
conn = sqlite3.connect("AnimalKingdom.db")
cursor = conn.cursor()

# Створення таблиці
cursor.execute("""
CREATE TABLE IF NOT EXISTS Animals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT
)
""")

# Очищаємо таблицю (щоб не дублювались дані при повторному запуску)
cursor.execute("DELETE FROM Animals")

# Додаємо записи
animals = [
    ("Лев", "Ссавець"),
    ("Крокодил", "Плазун"),
    ("Орел", "Птах"),
    ("Морська черепаха", "Плазун"),
    ("Мавпа", "Ссавець")
]

cursor.executemany("INSERT INTO Animals (name, type) VALUES (?, ?)", animals)

# Зміна назви "Орел" на "Сокіл"
cursor.execute("UPDATE Animals SET name = ? WHERE name = ?", ("Сокіл", "Орел"))

# Вибір всіх ссавців
print("Ссавці:")
cursor.execute("SELECT * FROM Animals WHERE type = ?", ("Ссавець",))
for row in cursor.fetchall():
    print(row)

print("\nУсі звірі:")
# Вивід усіх записів
cursor.execute("SELECT * FROM Animals")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
