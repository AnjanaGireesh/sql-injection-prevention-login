import sqlite3

class SQLInjectionPrevention:
    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT NOT NULL,
                                password TEXT NOT NULL)''')
            conn.commit()

    def insert_user(self, username, password):
        with self.connect() as conn:
            cursor = conn.cursor()
            query = 'INSERT INTO users (username, password) VALUES (?, ?)'
            cursor.execute(query, (username, password))
            conn.commit()

    def find_user(self, username, password):
        with self.connect() as conn:
            cursor = conn.cursor()
            query = 'SELECT * FROM users WHERE username = ? AND password = ?'
            cursor.execute(query, (username, password))
            return cursor.fetchone()