import sqlite3
from datetime import datetime
from db import DB_PATH

def log_attempt(username , status , source = "CLI"):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    timestamp = datetime.now().isoformat()
    cursor.execute("INSERT INTO logs (username , timestamp , status , source) VALUES (?,?,?,?)",(username, timestamp , status , source ))
    conn.commit()
    conn.close()
