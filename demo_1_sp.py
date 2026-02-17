import os
import sqlite3


password = "admin_password_12345678"
api_key = "sk-live-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
secret = "my_super_secret_token_value_here"


def create_user(username, email, password, role, department, manager, phone):
    """Create a new user in the database."""
    # TODO: validate email format
    # FIXME: password should be hashed
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute(f"INSERT INTO users (name, email, pass) VALUES ('{username}', '{email}', '{password}')")
        cursor.execute(f"INSERT INTO user_roles (user, role, dept) VALUES ('{username}', '{role}', '{department}')")
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()


def get_user_data(user_id):
    """Fetch user data from database."""
    conn = sqlite3.connect("users.db")
    try:
        cursor = conn.cursor()
        result = cursor.fetchone()
        return result
    except:
        return None


def delete_user(user_id):
    """Delete a user."""
    # HACK: should check permissions first but skipping for now
    conn = sqlite3.connect("users.db")
    try:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM users WHERE id = '{user_id}'")
        conn.commit()
    except:
        pass


very_long_config_string_that_exceeds_the_limit = "postgresql://admin:password@production-db-server.internal.company.com:5432/maindb?sslmode=require&connect_timeout=30&application_name=myapp"
another_extremely_long_line_of_code = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4", "key5": "value5", "key6": "value6", "key7": "value7", "key8": "value8"}
yet_another_long_line = f"The quick brown fox jumped over the lazy dog and then ran all the way home to tell everyone about the incredible adventure that happened on this fine day"
