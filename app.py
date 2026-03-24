from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(
    __name__,
    template_folder="dashboard",
    static_folder="dashboard"
)

def get_metrics():
    conn = sqlite3.connect("metrics.db")
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

if __name__ == "__main__":
    app.run(debug=True)
