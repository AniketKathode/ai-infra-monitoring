from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("metrics.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return {"message": "AI Infra Monitoring API is running"}

@app.route("/metrics/latest")
def latest_metrics():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM system_metrics
        ORDER BY timestamp DESC
        LIMIT 1
    """)

    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify(dict(row))
    return jsonify({"error": "No data found"})

@app.route("/metrics/history")
def metrics_history():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM system_metrics
        ORDER BY timestamp DESC
        LIMIT 50
    """)

    rows = cursor.fetchall()
    conn.close()

    return jsonify([dict(row) for row in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
