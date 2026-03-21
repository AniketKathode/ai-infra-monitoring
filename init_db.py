import sqlite3

conn = sqlite3.connect("metrics.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS system_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    cpu REAL,
    memory REAL,
    disk REAL
)
""")

conn.commit()
conn.close()

print("Database initialized successfully")
