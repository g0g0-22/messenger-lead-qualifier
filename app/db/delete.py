import sqlite3


def clear_all_data_and_reset_ids():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM messages")
    cursor.execute("DELETE FROM users")
    # Resets AUTOINCREMENT counters
    cursor.execute("DELETE FROM sqlite_sequence")

    conn.commit()
    conn.close()


clear_all_data_and_reset_ids()
