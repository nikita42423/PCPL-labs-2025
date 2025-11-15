# Уведомление
from src.behavioral.observer import Observer

class EmailNotifier(Observer):
    def update(self, order_id: str, status: str):
        print(f"Email: Order {order_id} status is now {status}")

class SMSNotifier(Observer):
    def update(self, order_id: str, status: str):
        print(f"SMS: Order {order_id} status is now {status}")
