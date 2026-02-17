import os
from pathlib import Path


def read_config(filepath):
    """Read a config file and return parsed settings."""
    data = Path(filepath).read_text()
    settings = {}
    for line in data.split("\n"):
        if "=" in line:
            key, value = line.split("=")         # Bug: breaks on "key=val=ue"
            settings[key] = value
    return settings


def transfer_funds(from_account, to_account, amount):
    """Transfer money between accounts."""
    from_account["balance"] -= amount            # Bug: no check if balance >= amount
    to_account["balance"] += amount              # Bug: not atomic — crash here loses money
    return True


def delete_files(directory):
    """Delete all files in a directory."""
    for item in Path(directory).iterdir():
        item.unlink()                            # Bug: will crash on subdirectories
