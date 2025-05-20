# Table for config_changes (id, timestamp, file, commit_hash, message)

# Table for rule_applications (id, timestamp, employee_id/json, rules_applied/json)

import sqlite3
import json
from datetime import datetime, timezone


DB_PATH = "log.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS config_changes(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   timestamp TEXT NOT NULL,
                   file TEXT NOT NULL,
                   commit_hash TEXT,
                   message TEXT
        )
                   """)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS rule_applications(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            employee TEXT NOT NULL,
            applied_rules TEXT
        )
        """
    )
    conn.commit()
    conn.close()

def log_config_change(file, commit_hash=None, message=None):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO config_changeS (timestamp, file, commit_hash, message) VALUES (?,?,?,?)" ,
    (datetime.now(timezone.utc).isoformat(),file,commit_hash, message),)
    conn.commit()
    conn.close()

def log_rules_application(employee, applied_rules):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO rule_applications (timestamp, employee, applied_rules) VALUES(?,?,?)",
        (
            datetime.now(timezone.utc).isoformat(),
            json.dumps(employee),
            json.dumps(applied_rules),
        ),

    )
    conn.commit()
    conn.close()