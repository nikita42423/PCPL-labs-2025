# Адаптер - структурный
from src.domain.payment import PaymentProcessor

class LegacyPaymentSystem:
    def make_payment(self, amount: float, card_number: str) -> bool:
        print(f"Processing payment of ${amount} via legacy system")
        return len(card_number) == 16

class PaymentAdapter(PaymentProcessor):
    def __init__(self, legacy_system: LegacyPaymentSystem):
        self.legacy_system = legacy_system

    def process_payment(self, order_id: str, amount: float, payment_details: dict) -> bool:
        card_number = payment_details.get('card_number', '')
        return self.legacy_system.make_payment(amount, card_number)
