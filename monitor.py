import psutil
import time
import sqlite3

conn = sqlite3.connect("metrics.db")
cursor = conn.cursor()

while True:
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    cursor.execute("""
        INSERT INTO system_metrics (cpu, memory, disk)
        VALUES (?, ?, ?)
    """, (cpu, memory, disk))

    conn.commit()

    print(f"Saved -> CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

    time.sleep(5)
