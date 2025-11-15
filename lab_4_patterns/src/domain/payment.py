# Оплата
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, order_id: str, amount: float, payment_details: dict) -> bool:
        pass
