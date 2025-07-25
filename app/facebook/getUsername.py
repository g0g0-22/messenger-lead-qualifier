import sqlite3
import requests
import os


def check_user(uid):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT COUNT(*) FROM users WHERE uid = ?
""", (uid,))
    n = cursor.fetchone()[0]
    conn.close()
    return n > 0


def get_username(uid):
    username = ""
    if check_user(uid):
        conn = sqlite3.connect("chatbot.db")
        cursor = conn.cursor()
        cursor.execute("""
        SELECT name FROM users WHERE uid = ?
         """, (uid,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else " "
    else:
        access_token = os.getenv("PAGE_ACCESS_TOKEN")
        print("Access token:", access_token)
        url = f"https://graph.facebook.com/{uid}"
        params = {
            "fields": "first_name,last_name",
            "access_token": access_token
        }
        response = requests.get(url=url, params=params)
        data = response.json()
        if "first_name" in data and "last_name" in data:
            return f"{data['first_name']}"
        else:
            return " "
