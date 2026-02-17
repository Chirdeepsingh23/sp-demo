import sqlite3

API_KEY = "sk-prod-abcdef1234567890abcdef1234"
token = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def get_user(user_id):
    """Look up a user by ID."""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = '{user_id}'")
    # TODO: close the connection properly
    return cursor.fetchone()
