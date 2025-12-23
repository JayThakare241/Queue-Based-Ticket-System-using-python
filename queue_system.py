from collections import deque
from models import Customer

class QueueSystem:
    def __init__(self):
        self.queue = deque()
        self.ticket_counter = 1

    def issue_ticket(self, name, vip=False):
        customer = Customer(name, self.ticket_counter, vip)
        self.ticket_counter += 1

        if vip:
            self.queue.appendleft(customer)
        else:
            self.queue.append(customer)

        return customer

    def serve_customer(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def queue_list(self):
        return list(self.queue)

    def size(self):
        return len(self.queue)

    def position_of_ticket(self, ticket_no):
        for i, c in enumerate(self.queue):
            if c.ticket_no == ticket_no:
                return i
        return -1

qs = QueueSystem()
