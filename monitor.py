import psutil
import time
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "metrics.db")


def collect_metrics():
    while True:
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()

            cpu = psutil.cpu_percent()
            memory = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent

            cursor.execute("""
                INSERT INTO system_metrics (cpu, memory, disk)
                VALUES (?, ?, ?)
            """, (cpu, memory, disk))

            conn.commit()
            conn.close()

            print(f"Saved -> CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

        except Exception as e:
            print("Monitoring error:", e)

        time.sleep(5)