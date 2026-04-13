from flask import Flask, render_template, jsonify
import csv
import os

app = Flask(__name__, template_folder="templates")

LOG_FILE = "file_events.csv"


# Home route → loads your dashboard
@app.route("/")
def index():
    return render_template("index.html")


# API route → returns logs in JSON format
@app.route("/logs")
def get_logs():
    logs = []

    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    logs.append({
                        "timestamp": row.get("timestamp", ""),
                        "event_type": row.get("event_type", ""),
                        "source_path": row.get("source_path", ""),
                        "destination_path": row.get("destination_path", "")
                    })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(logs)


# Health check (important for Render)
@app.route("/health")
def health():
    return {"status": "ok"}


# Run locally
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)