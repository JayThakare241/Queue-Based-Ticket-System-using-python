Queue-Based Ticket System (Python)

1. Project Overview

This project simulates a real-world ticket counter system using Queue Data Structure.
Customers are served on a FIFO basis, with support for VIP priority, estimated waiting time, and data storage.


2. Features

Queue-based ticket allocation

VIP & Normal priority queue

Estimated waiting time calculation

Command Line Interface (CLI)

Tkinter-based GUI application

Flask-based Web application

Ticket data stored in CSV & JSON



3. Data Structures Used

Queue (FIFO)

Priority Queue (VIP first)

Deque (efficient insertion & deletion)


4. Technologies

Python

Tkinter

Flask

CSV / JSON


5. How to Run
Install dependency
pip install -r requirements.txt
Run CLI version
python run_cli.py
Run GUI version
python gui_app.py
Run Web version
python web_app.py

Open browser: http://127.0.0.1:5000


6. Project Structure
queue_ticket_system/
│── models.py
│── queue_ds.py
│── storage.py
│── utils.py
│── run_cli.py
│── gui_app.py
│── web_app.py
│── requirements.txt
│── avg_service_time.txt
│── README.md
│── report.md


7. Learning Outcomes

Practical implementation of queue data structure

Understanding priority queues

Real-world system simulation

File handling using CSV & JSON



8. Conclusion

This project demonstrates the effective use of data structures in real-world applications like ticket management systems.