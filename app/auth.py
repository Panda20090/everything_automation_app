import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def create_user_table():
    conn = sqlite3.connect('data_automation.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def register_user(username, password):
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    conn = sqlite3.connect('data_automation.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()

def verify_user(username, password):
    conn = sqlite3.connect('data_automation.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    if user is None:
        return False
    return check_password_hash(user[0], password)
