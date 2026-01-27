import sqlite3
from passlib.hash import bcrypt

username = input("Enter the username: ")
password = input("Enter the password: ")


password_hashed = bcrypt.hash(password[:72])

conn = sqlite3.connect("auth.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,p
    username TEXT UNIQUE,
    password_hash TEXT
)
""")


try:
    cursor.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username, password_hashed)
    )
    conn.commit()
    

except sqlite3.IntegrityError:
    print(" Username already exists.")

conn.close()
