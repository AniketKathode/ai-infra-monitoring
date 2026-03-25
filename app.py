from flask import Flask, render_template, jsonify

import sqlite3
import os

# NEW: import anomaly detection
from analytics.anomaly import detect_anomalies

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "dashboard"),
    static_folder=os.path.join(BASE_DIR, "dashboard")
)

DB_PATH = os.path.join(BASE_DIR, "metrics.db")


def get_metrics():
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

    data = []
    for row in rows:
        data.append({
            "id": row[0],
            "cpu": row[1],
            "memory": row[2],
            "disk": row[3],
            "timestamp": row[4]
        })

    return list(reversed(data))


@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/metrics/history")
def history():
    return jsonify(get_metrics())


# NEW ROUTE: AI anomaly detection
@app.route("/metrics/anomalies")
def anomaly_history():
    from analytics.anomaly import detect_anomalies
    return jsonify(detect_anomalies())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)