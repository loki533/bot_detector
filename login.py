import sqlite3
from datetime import datetime
from passlib.hash import argon2
from db import DB_PATH
from logger import log_attempt

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

    if argon2.verify(password, stored_hash):
        print("Successful login")
        status = "SUCCESS"
    else:
        print("Wrong password")
        status = "FAIL"

# log the attempt
log_attempt(username, status)

# show logs (debug)
cursor.execute("SELECT * FROM logs")
rows = cursor.fetchall()

if rows:
    print("\nLogs:")
    for row in rows:
        print(row)

conn.commit()
conn.close()
