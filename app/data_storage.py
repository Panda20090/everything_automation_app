import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_data(conn, table, data):
    columns = ', '.join(data.keys())
    placeholders = ', '.join('?' * len(data))
    sql = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
    cur = conn.cursor()
    cur.execute(sql, list(data.values()))
    conn.commit()
    return cur.lastrowid

def query_data(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def setup_database():
    database = "data/data_automation.db"

    sql_create_google_trends_table = """
    CREATE TABLE IF NOT EXISTS google_trends (
        id integer PRIMARY KEY,
        date text NOT NULL,
        value real
    );"""

    sql_create_twitter_table = """
    CREATE TABLE IF NOT EXISTS twitter (
        id integer PRIMARY KEY,
        created_at text,
        text text
    );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_google_trends_table)
        create_table(conn, sql_create_twitter_table)
    else:
        print("Error! Cannot create the database connection.")

    return conn
