import sqlite3

def connect():
    return sqlite3.connect("learning.db")

def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        level INTEGER,
        xp INTEGER,
        streak INTEGER,
        weak_topic TEXT
    )
    """)

    conn.commit()
    conn.close()

