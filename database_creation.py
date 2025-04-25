import sqlite3

conn = sqlite3.connect('my_blogs.db')
c = conn.cursor()

# Create database users
conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        ''')

# დავამატოთ თუ არ არსებობს birthday_time column-ი
try:
    conn.execute('ALTER TABLE users ADD COLUMN birthday_time TEXT')
except sqlite3.OperationalError:
    pass

# Create user
conn.execute('''
    INSERT INTO users (username, email, age) VALUES ('Sandro Makatsara', 'sandro@gmail.com', 17)
''')
conn.commit()

# Update user
conn.execute('''
    UPDATE users SET age = 15 WHERE email = 'sandro@gmail.com'
''')
conn.commit()

# წავშალოთ კონკრეტული იუზერი
conn.execute('''
    DELETE FROM users WHERE id = 1
''')
conn.commit()

conn.close()