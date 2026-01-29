import sqlite3
from passlib.hash import argon2
from db import DB_PATH
from logger import log_attempt
from detector import is_suspicious

print("USING DB:", DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

username = input("Enter the username: ")
password = input("Enter the password: ")

cursor.execute(
    "SELECT password_hash FROM users WHERE username = ?",
    (username,)
)
result = cursor.fetchone()

if result is None:
    print("User not found")
    status = "FAIL"
else:
    stored_hash = result[0]

    try:
        if argon2.verify(password, stored_hash):
            print("Successful login")
            status = "SUCCESS"
        else:
            print("Wrong password")
            status = "FAIL"
    except ValueError:
        print("Invalid password hash")
        status = "FAIL"

log_attempt(username, status)

if is_suspicious(username):
    print("Too many failed attempts. Possible bot detected!")


conn.commit()
conn.close()
