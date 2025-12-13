from queue_ds import PriorityQueueSystem
from storage import save_enqueue, save_dequeue
from utils import estimated_wait_minutes

qs = PriorityQueueSystem()

while True:
    print("\n--- Ticket Counter System (CLI) ---")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. View Next Customer")
    print("4. Queue Size")
    print("5. View Full Queue")
    print("6. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        name = input("Customer name: ").strip()
        vip = input("Is VIP? (y/n): ").strip().lower() == "y"

        customer = qs.issue_ticket(name, vip)
        save_enqueue(customer)

        position = qs.position_of_ticket(customer.ticket_no)
        wait = estimated_wait_minutes(position)

        print(f"Ticket Issued: {customer}")
        print(f"Position in queue: {position + 1}")
        print(f"Estimated wait time: {wait} minutes")

    elif choice == "2":
        served = qs.serve_customer()
        if served:
            save_dequeue(served)
            print(f"Serving customer: {served}")
        else:
            print("No customers in queue.")

    elif choice == "3":
        next_customer = qs.peek_next()
        if next_customer:
            pos = qs.position_of_ticket(next_customer.ticket_no)
            print(f"Next customer: {next_customer}")
            print(f"Position: {pos + 1}")
        else:
            print("Queue is empty.")

    elif choice == "4":
        print("Total customers in queue:", qs.size())

    elif choice == "5":
        if qs.size() == 0:
            print("Queue is empty.")
        else:
            for i, c in enumerate(qs.queue_list(), start=1):
                print(f"{i}. {c}")

    elif choice == "6":
        print("Exiting system.")
        break

    else:
        print("Invalid choice. Try again.")
