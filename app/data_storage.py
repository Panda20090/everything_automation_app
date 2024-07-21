import sqlite3

def setup_database():
    conn = sqlite3.connect('data/data_automation.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS google_trends (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            value INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS twitter (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT,
            text TEXT
        )
    ''')
    conn.commit()
    return conn

def insert_data(conn, table, data):
    cursor = conn.cursor()
    placeholders = ', '.join(['?'] * len(data))
    columns = ', '.join(data.keys())
    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
    cursor.execute(sql, list(data.values()))
    conn.commit()

def query_data(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
