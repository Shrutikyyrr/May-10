import sqlite3

DB_NAME = "library.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    c = conn.cursor()

    # Books Table
    c.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            isbn TEXT UNIQUE,
            quantity INTEGER,
            available INTEGER
        )
    """)

    # Members Table
    c.execute("""
        CREATE TABLE IF NOT EXISTS members(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE
        )
    """)

    # Borrow Records
    c.execute("""
        CREATE TABLE IF NOT EXISTS borrow_records(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER,
            book_id INTEGER,
            borrow_date TEXT,
            return_date TEXT,
            status TEXT
        )
    """)

    # Logs Table
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()