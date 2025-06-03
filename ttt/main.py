import pandas as pd
import sqlite3

# Создание DataFrame
df = pd.DataFrame({
    'name': ['Анна', 'Борис'],
    'age': [25, 30]
})

# Сохранение в SQLite
conn = sqlite3.connect('pandas_db.db')
df.to_sql('users', conn, if_exists='replace', index=False)

# Чтение из БД обратно в DataFrame
df_from_db = pd.read_sql("SELECT * FROM users", conn)
print(df_from_db)