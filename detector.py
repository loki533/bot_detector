import sqlite3
from datetime import datetime, timedelta
from db import DB_PATH

MAX_FAILED = 5
WINDOW_SECONDS = 60

def is_suspicious(username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    time_limit = (datetime.now() - timedelta(seconds=WINDOW_SECONDS)).isoformat()

    cursor.execute("""
        SELECT COUNT(*) FROM logs
        WHERE username = ?
        AND status = 'FAIL'
        AND timestamp >= ?
    """, (username, time_limit))

    count = cursor.fetchone()[0]
    conn.close()

    return count >= MAX_FAILED
