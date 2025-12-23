class Customer:
    def __init__(self, name, ticket_no, vip=False):
        self.name = name
        self.ticket_no = ticket_no
        self.vip = vip

    def __str__(self):
        return f"{self.name} (T{self.ticket_no}){' [VIP]' if self.vip else ''}"
