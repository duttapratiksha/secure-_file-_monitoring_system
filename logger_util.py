import csv
import os
from datetime import datetime

LOG_FILE = "file_events.csv"

def create_log_file():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "event_type",
                "source_path",
                "destination_path",
                "status",
                "integrity"
            ])

def write_log(event_type, src, dest="", status="SAFE", integrity="OK"):
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            event_type,
            src,
            dest,
            status,
            integrity
        ])