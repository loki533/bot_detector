import sqlite3

conn = sqlite3.connect("auth.db")
cursor = conn.cursor()

cursor.execute(""" 
               CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT UNIQUE NOT NULL,
               password_hash STRING NOT NULL)""")

cursor.execute("""
               CREATE TABLE IF NOT EXISTS logs
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT,
               timestamp TEXT,
               source TEXT,
               status TEXT)
               """)

conn.commit()
conn.close()

print("Database initialized.")