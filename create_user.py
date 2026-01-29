import sqlite3
from passlib.hash import argon2
from db import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

password_hash = argon2.hash(password)

cursor.execute(
    "INSERT INTO users (username, password_hash) VALUES (?, ?)",
    (username, password_hash)
)

conn.commit()
conn.close()

print("User registered successfully")
