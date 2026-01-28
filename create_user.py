import sqlite3
import os
from passlib.hash import bcrypt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "auth.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

username = input("Enter the username: ")
password = input("Enter the password: ")

password_hashed = bcrypt.hash(password[:72])

try:
    cursor.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username, password_hashed)
    )
    conn.commit()
    print("User created successfully")

except sqlite3.IntegrityError:
    print("Username already exists")

conn.close()
