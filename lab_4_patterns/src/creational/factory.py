# Фабрика (создание) - порождающий
from abc import ABC, abstractmethod
from src.domain.order import Order

class OrderFactory(ABC):
    @abstractmethod
    def create_order(self, order_data: dict) -> Order:
        pass

class StandardOrderFactory(OrderFactory):
    def create_order(self, order_data: dict) -> Order:
        return Order(
            id=order_data['id'],
            customer_name=order_data['customer_name'],
            items=order_data['items'],
            total_amount=order_data['total_amount']
        )

class ExpressOrderFactory(OrderFactory):
    def create_order(self, order_data: dict) -> Order:
        order = Order(
            id=order_data['id'],
            customer_name=order_data['customer_name'],
            items=order_data['items'],
            total_amount=order_data['total_amount']
        )
        order.express_delivery = True
        order.shipping_cost = order_data.get('shipping_cost', 15.0)
        return order
