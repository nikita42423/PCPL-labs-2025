import pytest
from src.creational.factory import StandardOrderFactory, ExpressOrderFactory

class TestOrderFactory:
    def test_standard_order_creation(self):
        # Arrange
        factory = StandardOrderFactory()
        order_data = {
            'id': '123',
            'customer_name': 'John Doe',
            'items': ['item1', 'item2'],
            'total_amount': 100.0
        }

        # Act
        order = factory.create_order(order_data)

        # Assert
        assert order.id == '123'
        assert order.customer_name == 'John Doe'
        assert order.total_amount == 100.0
        assert order.express_delivery == False

    def test_express_order_creation(self):
        # Arrange
        factory = ExpressOrderFactory()
        order_data = {
            'id': '124',
            'customer_name': 'Jane Smith',
            'items': ['item1'],
            'total_amount': 50.0,
            'shipping_cost': 15.0
        }

        # Act
        order = factory.create_order(order_data)

        # Assert
        assert order.id == '124'
        assert order.express_delivery == True
        assert order.shipping_cost == 15.0
