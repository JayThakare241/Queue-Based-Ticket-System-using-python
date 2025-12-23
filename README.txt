QUEUE BASED TICKET SYSTEM
========================

PROJECT DESCRIPTION
-------------------
This project is a Queue Based Ticket System developed using Python and Tkinter.
It follows the FIFO (First In First Out) principle with VIP priority support.
The system allows users to generate tickets, serve customers, and store ticket
information permanently in a CSV file.

The project demonstrates the use of:
- Data Structures (Queue)
- Object Oriented Programming (OOPS)
- GUI programming using Tkinter
- File handling using CSV

--------------------------------------------------

FEATURES
--------
1. Generate ticket for customers
2. VIP customers get priority
3. Serve customers in queue order
4. Automatic ticket number generation
5. Estimated waiting time calculation
6. Ticket data saved in CSV file (Excel compatible)
7. User-friendly graphical interface

--------------------------------------------------

PROJECT STRUCTURE
-----------------
Queue based Ticket System/
│
├── gui_app.py        -> Main GUI application (Run this file)
├── queue_system.py  -> Queue implementation (DSA)
├── models.py        -> Customer class (OOPS)
├── utils.py         -> Waiting time calculation
├── csv_storage.py   -> CSV file storage logic
├── tickets.csv      -> Auto-generated ticket data file
└── README.txt       -> Project documentation

--------------------------------------------------

REQUIREMENTS
------------
- Python 3.x
- Tkinter (comes pre-installed with Python)

No external libraries are required.

--------------------------------------------------

HOW TO RUN THE PROJECT
----------------------
1. Open Command Prompt
2. Navigate to the project folder
3. Run the following command:

   py gui_app.py

4. The GUI window will open.

--------------------------------------------------

HOW DATA IS STORED
------------------
All generated tickets are stored in a CSV file named:

tickets.csv

Each record contains:
- Ticket Number
- Customer Name
- VIP status
- Ticket Status (WAITING / SERVED)

The CSV file can be opened directly in Microsoft Excel.

--------------------------------------------------

QUEUE WORKING
-------------
- Normal customers are added at the end of the queue
- VIP customers are added at the front of the queue
- Customers are served using FIFO principle

--------------------------------------------------

VIVA / INTERVIEW SUMMARY
------------------------
This project implements a queue-based ticket system using Python.
It uses Tkinter for GUI, deque for queue operations, OOPS for customer
modeling, and CSV for persistent data storage.

--------------------------------------------------

AUTHOR
------
Developed by: <Your Name>
Course: MCA / BCA
Subject: Data Structures / Python Programming

--------------------------------------------------
