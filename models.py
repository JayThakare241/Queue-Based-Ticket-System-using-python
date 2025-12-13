from datetime import datetime


class Customer:
    def __init__(self, ticket_no, name, is_vip=False):
        self.ticket_no = ticket_no
        self.name = name
        self.is_vip = is_vip
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        vip_tag = " (VIP)" if self.is_vip else ""
        return f"#{self.ticket_no}{vip_tag} - {self.name}"
