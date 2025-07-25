import sqlite3


def init_db():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        uid TEXT PRIMARY KEY,
        name TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP          
        )
                   
                   """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uid TEXT,
        sender TEXT,
        text TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(uid) REFERENCES users(uid)
        )
    """)
    conn.commit()
    conn.close()


def add_message(uid, name, sender, text):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO users (uid, name) VALUES (?,?)", (uid, name))
    cursor.execute(
        "INSERT INTO messages (uid, sender, text) VALUES (?,?,?)", (uid, sender, text))
    conn.commit()
    conn.close()


def get_conversation(uid, limit=10):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT sender, text FROM messages
    WHERE uid = ?
    ORDER BY timestamp DESC
    LIMIT ?
    """, (uid, limit))
    rows = cursor.fetchall()
    conn.close()
    return rows[::-1]
