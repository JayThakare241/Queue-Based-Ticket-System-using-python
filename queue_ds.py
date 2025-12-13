from collections import deque
from models import Customer


class PriorityQueueSystem:
    """
    Two-level queue:
    - VIP customers served first
    - FIFO within each queue
    """

    def __init__(self):
        self.vip_q = deque()
        self.normal_q = deque()
        self._next_ticket = 1

    def issue_ticket(self, name, is_vip=False):
        customer = Customer(self._next_ticket, name, is_vip)
        self._next_ticket += 1

        if is_vip:
            self.vip_q.append(customer)
        else:
            self.normal_q.append(customer)

        return customer

    def serve_customer(self):
        if self.vip_q:
            return self.vip_q.popleft()
        elif self.normal_q:
            return self.normal_q.popleft()
        else:
            return None

    def peek_next(self):
        if self.vip_q:
            return self.vip_q[0]
        elif self.normal_q:
            return self.normal_q[0]
        else:
            return None

    def size(self):
        return len(self.vip_q) + len(self.normal_q)

    def queue_list(self):
        return list(self.vip_q) + list(self.normal_q)

    def position_of_ticket(self, ticket_no):
        for index, customer in enumerate(self.queue_list()):
            if customer.ticket_no == ticket_no:
                return index
        return -1
