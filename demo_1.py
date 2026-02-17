import os
import sqlite3

API_KEY = os.environ.get("API_KEY")
token = os.environ.get("token")

def get_user(user_id):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM users WHERE id = '{user_id}'")
        return cursor.fetchone()
    finally:
        conn.close()
