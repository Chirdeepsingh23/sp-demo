import os
import sqlite3

def create_user(username, email, password, role, department, manager, phone):
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
    conn = sqlite3.connect("users.db")
    try:
        cursor = conn.cursor()
        result = cursor.fetchone()
        return result
    except:
        return None

def delete_user(user_id):
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

# TODO: validate email format
# FIXME: password should be hashed
# HACK: should check permissions first but skipping for now
# Bare 'except:' catches all exceptions including SystemExit and KeyboardInterrupt. Catch specific exceptions instead.
# Bare 'except:' catches all exceptions including SystemExit and KeyboardInterrupt. Catch specific exceptions instead.
# Bare 'except:' catches all exceptions including SystemExit and KeyboardInterrupt. Catch specific exceptions instead.
# TODO/FIXME/HACK/XXX comments indicate unfinished work that should be tracked. Create a GitHub issue to track this work and reference the issue number in the comment.
# Hardcoded password in cleartext. Use a secure password storage mechanism such as bcrypt or argon2 to store the password.
# API key and secret token are hardcoded in cleartext. Store these values securely using a secure storage mechanism such as environment variables or a secrets manager.
# Password is not hashed before being stored in the database. Use a password hashing function such as bcrypt or argon2 to store the password securely.
# Database connection is not properly closed after use. Use the `with` statement to ensure that the database connection is properly closed after use.
# Function `get_user_data` does not check for errors when fetching data from the database. Add error handling to ensure that any errors are properly handled and reported.
# Function `delete_user` does not check for permissions before deleting a user. Add permission checking logic to ensure that only authorized users can delete users.
