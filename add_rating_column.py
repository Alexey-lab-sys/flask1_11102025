import sqlite3
from pathlib import Path

# Укажите путь к вашей базе данных
BASE_DIR = Path(__file__).parent
path_to_db = BASE_DIR / "new_store.db"

# Подключение к базе данных
conn = sqlite3.connect(path_to_db)
cursor = conn.cursor()

# Команда для добавления колонки
try:
    cursor.execute("ALTER TABLE quotes ADD COLUMN rating INTEGER DEFAULT 1;")  # Добавляем колонку
    print("Колонка 'rating' успешно добавлена.")
except sqlite3.OperationalError as e:
    print(f"Ошибка: {str(e)}")  # Если ошибка, выводим сообщение

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
