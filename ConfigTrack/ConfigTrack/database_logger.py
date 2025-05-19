import sqlite3
from datetime import datetime

DB_NAME = 'log.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''

            CREATE TABLE IF NOT EXISTS logs(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   action TEXT,
                   file_name TEXT,
                   timestamp TEXT
            )
                   ''')
    conn.commit()
    conn.close()

def log_action(action, file_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(
        'INSERT INTO logs (action, file_name, timestamp) VALUES(?,?,?)',
            (action, file_name,timestamp)
        )
    conn.commit()
    conn.close()