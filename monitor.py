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
import psutil
import time
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "metrics.db")


def collect_metrics():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
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