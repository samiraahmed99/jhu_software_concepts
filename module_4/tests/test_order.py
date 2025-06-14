"""
Unit tests for the Order class.
"""

import pytest
from src.order import Order
from src.pizza import Pizza


@pytest.mark.order
def test_order__init__():
    """
    GIVEN a new Order
    WHEN it is created
    THEN it should start with no pizzas, zero cost, and unpaid
    """
    order = Order()
    assert isinstance(order.pizzas, list)
    assert len(order.pizzas) == 0
    assert order.total == 0.0
    assert order.paid is False

@pytest.mark.order
def test_order__str__():
    """
    GIVEN an order with one pizza
    WHEN str() is called
    THEN the result should include the pizza and total cost
    """
    order = Order()
    order.input_pizza("Thin", "Marinara", "Mozzarella", ["Pepperoni"])
    result = str(order)
    assert "Thin" in result
    assert "Marinara" in result
    assert "Pepperoni" in result
    assert f"${order.total:.2f}" in result

@pytest.mark.order
def test_order_input_pizza():
    """
    GIVEN an order
    WHEN a pizza is added
    THEN the order total should update correctly
    """
    order = Order()
    order.input_pizza("Thick", "Pesto", "Mozzarella", ["Mushrooms"])
    assert len(order.pizzas) == 1
    assert order.total > 0

@pytest.mark.order
def test_order_paid():
    """
    GIVEN an unpaid order
    WHEN order_paid() is called
    THEN paid status should become True
    """
    order = Order()
    order.order_paid()
    assert order.paid is True
