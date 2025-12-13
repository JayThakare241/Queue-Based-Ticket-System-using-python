import csv
import json
from pathlib import Path
from datetime import datetime

CSV_FILE = Path("tickets_history.csv")
JSON_FILE = Path("tickets_history.json")


def save_enqueue(customer):
    record = {
        "ticket_no": customer.ticket_no,
        "name": customer.name,
        "is_vip": customer.is_vip,
        "action": "ENQUEUE",
        "timestamp": customer.created_at
    }

    _save_csv(record)
    _save_json(record)


def save_dequeue(customer):
    record = {
        "ticket_no": customer.ticket_no,
        "name": customer.name,
        "is_vip": customer.is_vip,
        "action": "DEQUEUE",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    _save_csv(record)
    _save_json(record)


def _save_csv(record):
    file_exists = CSV_FILE.exists()

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["ticket_no", "name", "is_vip", "action", "timestamp"]
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(record)


def _save_json(record):
    data = []

    if JSON_FILE.exists():
        try:
            with open(JSON_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError:
            data = []

    data.append(record)

    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
