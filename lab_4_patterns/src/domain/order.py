# Заказ
class Order:
    def __init__(self, id: str, customer_name: str, items: list, total_amount: float):
        self.id = id
        self.customer_name = customer_name
        self.items = items
        self.total_amount = total_amount
        self.status = "created"
        self.express_delivery = False
        self.shipping_cost = 0.0

    def update_status(self, new_status: str):
        self.status = new_status
        return self
