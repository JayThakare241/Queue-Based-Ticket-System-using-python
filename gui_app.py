import tkinter as tk
from tkinter import ttk, messagebox

from queue_system import qs
from utils import estimated_wait_minutes
from csv_storage import init_csv, save_ticket, update_status


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Queue Based Ticket System")
        self.geometry("500x400")

        init_csv()   # create CSV file if not exists
        self.build_ui()

    def build_ui(self):
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Customer Name").grid(row=0, column=0)
        self.name_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.name_var).grid(row=0, column=1)

        self.vip_var = tk.BooleanVar()
        ttk.Checkbutton(frame, text="VIP", variable=self.vip_var).grid(row=0, column=2)

        ttk.Button(frame, text="Add Customer", command=self.add_customer).grid(row=1, column=0)
        ttk.Button(frame, text="Serve Customer", command=self.serve_customer).grid(row=1, column=1)
        ttk.Button(frame, text="Refresh Queue", command=self.refresh).grid(row=1, column=2)

        self.listbox = tk.Listbox(frame, height=12)
        self.listbox.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=10)

        self.status = ttk.Label(self, text="Queue size: 0")
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

        self.refresh()

    def add_customer(self):
        name = self.name_var.get().strip()
        if not name:
            messagebox.showwarning("Error", "Enter customer name")
            return

        customer = qs.issue_ticket(name, self.vip_var.get())
        save_ticket(customer)

        pos = qs.position_of_ticket(customer.ticket_no)
        wait = estimated_wait_minutes(pos)

        messagebox.showinfo(
            "Ticket Issued",
            f"{customer}\nPosition: {pos + 1}\nEstimated wait: {wait} min"
        )

        self.name_var.set("")
        self.vip_var.set(False)
        self.refresh()

    def serve_customer(self):
        customer = qs.serve_customer()
        if customer:
            update_status(customer.ticket_no)
            messagebox.showinfo("Serving", f"Now serving:\n{customer}")
        else:
            messagebox.showinfo("Info", "Queue is empty")

        self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)

        if qs.size() == 0:
            self.listbox.insert(tk.END, "Queue is empty")
        else:
            for i, c in enumerate(qs.queue_list(), start=1):
                wait = estimated_wait_minutes(i - 1)
                self.listbox.insert(
                    tk.END, f"{i}. {c} | Est wait: {wait} min"
                )

        self.status.config(text=f"Queue size: {qs.size()}")


if __name__ == "__main__":
    App().mainloop()
