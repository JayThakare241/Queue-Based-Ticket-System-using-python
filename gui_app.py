# gui_app.py
class App(tk.Tk):
def __init__(self):
super().__init__()
self.title('Ticket Counter (Tkinter)')
self.geometry('500x400')
self._build()


def _build(self):
frm = ttk.Frame(self, padding=10)
frm.pack(fill=tk.BOTH, expand=True)


ttk.Label(frm, text='Customer name:').grid(row=0, column=0, sticky='w')
self.name_var = tk.StringVar()
ttk.Entry(frm, textvariable=self.name_var).grid(row=0, column=1, sticky='ew')


self.is_vip = tk.BooleanVar()
ttk.Checkbutton(frm, text='VIP', variable=self.is_vip).grid(row=0, column=2)


ttk.Button(frm, text='Add Customer', command=self.add_customer).grid(row=1, column=0)
ttk.Button(frm, text='Serve Customer', command=self.serve_customer).grid(row=1, column=1)
ttk.Button(frm, text='Refresh Queue', command=self.refresh_queue).grid(row=1, column=2)


self.queue_listbox = tk.Listbox(frm, height=12)
self.queue_listbox.grid(row=2, column=0, columnspan=3, sticky='nsew', pady=10)


frm.columnconfigure(1, weight=1)
frm.rowconfigure(2, weight=1)


self.status_label = ttk.Label(self, text='Queue size: 0')
self.status_label.pack(side=tk.BOTTOM, fill=tk.X)


def add_customer(self):
name = self.name_var.get().strip()
if not name:
messagebox.showwarning('Input', 'Enter name')
return
c = qs.issue_ticket(name, self.is_vip.get())
save_enqueue(c)
pos = qs.position_of_ticket(c.ticket_no)
wait = estimated_wait_minutes(pos)
messagebox.showinfo('Ticket issued', f'Issued {c}\nPosition: {pos+1}\nEst wait: {wait} minutes')
self.name_var.set('')
self.is_vip.set(False)
self.refresh_queue()


def serve_customer(self):
s = qs.serve_customer()
if s:
save_dequeue(s)
messagebox.showinfo('Serving', f'Serving: {s}')
else:
messagebox.showinfo('Info', 'No customers in queue')
self.refresh_queue()


def refresh_queue(self):
self.queue_listbox.delete(0, tk.END)
for i, c in enumerate(qs.queue_list(), start=1):
pos = i-1
wait = estimated_wait_minutes(pos)
self.queue_listbox.insert(tk.END, f'{i}. {c} - est wait: {wait} min')
self.status_label.config(text=f'Queue size: {qs.size()}')


if __name__ == '__main__':
App().mainloop()