from pytest_bdd import scenarios, given, when, then
from src.creational.factory import StandardOrderFactory, ExpressOrderFactory

scenarios('order_creation.feature')

@given('I have order data for a standard order')
def standard_order_data():
    return {
        'id': '123',
        'customer_name': 'John Doe',
        'items': ['item1', 'item2'],
        'total_amount': 100.0
    }

@given('I have order data for an express order')
def express_order_data():
    return {
        'id': '124',
        'customer_name': 'Jane Smith',
        'items': ['item1'],
        'total_amount': 50.0,
        'shipping_cost': 15.0
    }

@when('I create an order using StandardOrderFactory')
def create_standard_order(standard_order_data):
    factory = StandardOrderFactory()
    return factory.create_order(standard_order_data)

@when('I create an order using ExpressOrderFactory')
def create_express_order(express_order_data):
    factory = ExpressOrderFactory()
    return factory.create_order(express_order_data)

@then('the order should be created with correct details')
def verify_order_created(order):
    assert order.id is not None
    assert order.customer_name is not None
    assert len(order.items) > 0

@then('the order should not have express delivery')
def verify_standard_order(order):
    assert order.express_delivery == False

@then('the order should have express delivery enabled')
def verify_express_order(order):
    assert order.express_delivery == True
