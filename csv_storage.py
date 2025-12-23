import csv
import os

FILE_NAME = "tickets.csv"

def init_csv():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Ticket No", "Name", "VIP", "Status"])

def save_ticket(customer):
    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            customer.ticket_no,
            customer.name,
            "YES" if customer.vip else "NO",
            "WAITING"
        ])

def update_status(ticket_no):
    rows = []

    with open(FILE_NAME, "r", newline="") as f:
        rows = list(csv.reader(f))

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            if row and row[0] == str(ticket_no):
                row[3] = "SERVED"
            writer.writerow(row)
