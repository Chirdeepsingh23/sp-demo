import os
from pathlib import Path

def read_config(filepath):
    data = Path(filepath).read_text()
    settings = {}
    for line in data.split("\n"):
        if "=" in line:
            key, value = line.split("=", 1) # Bug fix: use split with maxsplit=1 to avoid breaking on 'key=val=ue'
            settings[key] = value
    return settings

def transfer_funds(from_account, to_account, amount):
    if from_account["balance"] >= amount: # Bug fix: add check for sufficient balance
        from_account["balance"] -= amount
        to_account["balance"] += amount
        return True
    else:
        return False

def delete_files(directory):
    for item in os.walk(directory): # Bug fix: use os.walk() to iterate over all files and directories recursively
        if item.is_file():
            item.unlink()

# Test cases
assert read_config("config.txt") == {"key1": "value1", "key2": "value2"}
assert transfer_funds({"balance": 10}, {"balance": 5}, 3) == True
assert delete_files("/path/to/directory") == None

# Output:
# Python code only (no text, comments, or markers)
import os
from pathlib import Path

def read_config(filepath):
    data = Path(filepath).read_text()
    settings = {}
    for line in data.split("\n"):
        if "=" in line:
            key, value = line.split("=", 1) # Bug fix: use split with maxsplit=1 to avoid breaking on 'key=val=ue'
            settings[key] = value
    return settings

def transfer_funds(from_account, to_account, amount):
    if from_account["balance"] >= amount: # Bug fix: add check for sufficient balance
        from_account["balance"] -= amount
        to_account["balance"] += amount
        return True
    else:
        return False

def delete_files(directory):
    for item in os.walk(directory): # Bug fix: use os.walk() to iterate over all files and directories recursively
        if item.is_file():
            item.unlink()

# Test cases
assert read_config("config.txt") == {"key1": "value1", "key2": "value2"}
assert transfer_funds({"balance": 10}, {"balance": 5}, 3) == True
assert delete_files("/path/to/directory") == None
