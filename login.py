import sqlite3
from passlib.hash import bcrypt
from datetime import datetime
from db import DB_PATH

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
    if bcrypt.verify(password[:72], result[0]):
        print("Successful login")
        status = "SUCCESS"
    else:
        print("Wrong password")
        status = "FAIL"

timestamp = datetime.now().isoformat()

cursor.execute(
    "INSERT INTO logs (username, timestamp, source, status) VALUES (?, ?, ?, ?)",
    (username, timestamp, "CLI", status)
)

cursor.execute("SELECT * from logs")
result = cursor.fetchall()

if result:
    for result in result:
        print(result)


conn.commit()
conn.close()
