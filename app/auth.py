import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def create_user_table():
    conn = sqlite3.connect('data/data_automation.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect('data/data_automation.db')
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password, method='sha256')
    cursor.execute('''
        INSERT INTO users (username, password) VALUES (?, ?)
    ''', (username, hashed_password))
    conn.commit()
    conn.close()

def verify_user(username, password):
    conn = sqlite3.connect('data/data_automation.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT password FROM users WHERE username = ?
    ''', (username,))
    row = cursor.fetchone()
    conn.close()
    if row and check_password_hash(row[0], password):
        return True
    return False
