from flask import Flask, render_template, jsonify
import sqlite3
import os
import threading

# Import anomaly detection
from analytics.anomaly import detect_anomalies

# Import monitoring collector
from monitor import collect_metrics

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "dashboard"),
    static_folder=os.path.join(BASE_DIR, "dashboard")
)

DB_PATH = os.path.join(BASE_DIR, "metrics.db")


# -------------------------------
# Background monitoring thread
# -------------------------------
def start_monitor():
    collect_metrics()


# Start monitoring in background (works in Docker + Render)
threading.Thread(target=start_monitor, daemon=True).start()


# -------------------------------
# Database read function
# -------------------------------
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


# -------------------------------
# Routes
# -------------------------------
@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("index.html")


@app.route("/metrics/history")
def history():
    return jsonify(get_metrics())


@app.route("/metrics/anomalies")
def anomaly_history():
    return jsonify(detect_anomalies())


# Health check for Render
@app.route("/healthz")
def health():
    return "OK", 200


# -------------------------------
# Local development run
# -------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)