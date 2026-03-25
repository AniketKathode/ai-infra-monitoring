import sqlite3
import os
import numpy as np
from sklearn.ensemble import IsolationForest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "metrics.db")


def detect_anomalies():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, cpu, memory, disk, timestamp
        FROM system_metrics
        ORDER BY id DESC
        LIMIT 50
    """)

    rows = cursor.fetchall()
    conn.close()

    if len(rows) < 10:
        return []

    data = []
    for row in rows:
        data.append({
            "id": row[0],
            "cpu": row[1],
            "memory": row[2],
            "disk": row[3],
            "timestamp": row[4]
        })

    data.reverse()

    X = np.array([[d["cpu"], d["memory"], d["disk"]] for d in data])

    model = IsolationForest(contamination=0.1)
    model.fit(X)

    predictions = model.predict(X)

    anomalies = []
    for i, p in enumerate(predictions):
        if p == -1:
            anomalies.append(data[i])

    return anomalies