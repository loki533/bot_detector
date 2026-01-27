import sqlite3
conn = sqlite3.connect("auth.db")
cur = conn.cursor()
cur.execute("SELECT id, username FROM users")
print(cur.fetchall())
conn.close()
