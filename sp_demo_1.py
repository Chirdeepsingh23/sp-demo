# test_mixed_review.py
"""User account management module."""

import os

# SEC-001: hardcoded secret (x2)
DATABASE_PASSWORD = "SuperSecret123!"
API_TOKEN = "sk-live-abcdefghijklmnop"

# SEC-002: SQL injection
def get_user(user_id):
    import sqlite3
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = '{user_id}'")
    return cursor.fetchone()

# QLT-001: function too long (>50 lines)
def process_all_data(name, email, phone, address, city, zipcode):
    # QLT-002: too many arguments (6 > 5)
    result = {}
    result["name"] = name
    result["email"] = email
    result["phone"] = phone
    result["address"] = address
    result["city"] = city
    result["zipcode"] = zipcode
    result["full_address"] = address + " " + city + " " + zipcode
    result["display"] = name + " <" + email + ">"
    result["validated"] = False
    result["errors"] = []
    result["warnings"] = []
    result["status"] = "pending"
    result["retry_count"] = 0
    result["last_updated"] = None
    result["created_at"] = None
    result["modified_by"] = None
    result["version"] = 1
    result["is_active"] = True
    result["is_verified"] = False
    result["verification_code"] = None
    result["verification_sent"] = False
    result["login_count"] = 0
    result["last_login"] = None
    result["failed_logins"] = 0
    result["locked"] = False
    result["lock_reason"] = None
    result["preferences"] = {}
    result["notifications"] = True
    result["theme"] = "default"
    result["language"] = "en"
    result["timezone"] = "UTC"
    result["avatar_url"] = None
    result["bio"] = ""
    result["website"] = None
    result["social_links"] = {}
    result["tags"] = []
    result["groups"] = []
    result["permissions"] = []
    result["role"] = "user"
    result["department"] = None
    result["manager"] = None
    result["start_date"] = None
    result["end_date"] = None
    result["salary"] = None
    result["bonus"] = None
    result["review_score"] = None
    result["notes"] = ""
    result["attachments"] = []
    result["history"] = []
    result["metadata"] = {}
    return result

# BPR-001: bare except
def load_config():
    try:
        with open("config.json") as f:
            return f.read()
    except:
        return "{}"

# BPR-002: TODO
# TODO: add proper input validation later

# STY-001: line too long
def format_message(user, action, timestamp, details, metadata, extra_context, additional_info, supplementary_data):
    return f"User {user} performed {action} at {timestamp} with details {details} and metadata {metadata} and extra {extra_context} and additional {additional_info} and supplementary {supplementary_data}"


# --- LLM-only issues (static won't catch these) ---

def transfer_balance(from_account, to_account, amount):
    """Transfer money between accounts."""
    from_account["balance"] -= amount
    to_account["balance"] += amount
    # LLM should catch: no check if from_account has sufficient balance
    # LLM should catch: not atomic — if second line fails, money is lost


def find_average(numbers):
    """Calculate average of a list."""
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)
    # LLM should catch: ZeroDivisionError if numbers is empty
