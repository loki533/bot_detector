import sqlite3
from passlib.hash import bcrypt

username = input("Enter the username: ")
password = input("Enter the password:")

password_hashed = bcrypt.hash(password)

conn = sqlite3.connect("auth.db")
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO user (username , password_hash ) VALUES (?,?)",
                (username,password_hashed))
    #using ? as to prevent sql injection inserts it sepreatly

    conn.commit()
    print("Execution success")

except sqlite3.IntegrityError:
    print("Username already exists.")

conn.close()