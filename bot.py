print("🔥 attack.py file started")

import time
from passlib.hash import argon2
import sqlite3
from db import DB_PATH
from detector import is_suspicious
from logger import log_attempt

MAX_ATTEMPTS = 10
DELAY_SECONDS = 2

PASSWORDS = [
    "123456",
    "password",
    "admin",
    "loki13",
    "test123",
    "welcome"
]

def simulate_attack(username):
    print(f"🚨 Starting brute-force simulation on: {username}")

    attempts = 0
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for password in PASSWORDS:
        print(f"Trying password: {password}")

        if attempts >= MAX_ATTEMPTS:
            print("🛑 Maximum attempts reached")
            break

        if is_suspicious(username):
            print("🚨 Bot detected — stopping attack")
            break

        cursor.execute(
            "SELECT password_hash FROM users WHERE username = ?",
            (username,)
        )
        result = cursor.fetchone()

        if result is None:
            print("❌ User does not exist")
            log_attempt(username, "FAIL")
            break

        stored_hash = result[0]

        if argon2.verify(password, stored_hash):
            print("✅ Password cracked (simulation)")
            log_attempt(username, "SUCCESS")
            break
        else:
            print("❌ Failed attempt")
            log_attempt(username, "FAIL")

        attempts += 1
        time.sleep(DELAY_SECONDS)

    conn.close()
    print("✅ Simulation finished.")

simulate_attack("loki")
