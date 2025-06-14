"""
Integration tests for the pizza ordering system.
"""

import pytest
from src.order import Order
from src.pizza import Pizza


@pytest.mark.order
def test_multiple_pizzas_add_up_correctly_order_1():
    """
    GIVEN an order with two pizzas
    WHEN both pizzas are added
    THEN the total cost should be the sum of both pizzas
    """
    pizza1 = Pizza("Thin", "Pesto", "Mozzarella", ["Mushrooms"])
    pizza2 = Pizza("Thick", "Marinara", "Mozzarella", ["Mushrooms"])
    order = Order()
    order.pizzas.append(pizza1)
    order.pizzas.append(pizza2)
    order.total += pizza1.cost_value + pizza2.cost_value

    expected_total = pizza1.cost_value + pizza2.cost_value
    assert len(order.pizzas) == 2
    assert order.total == expected_total


@pytest.mark.order
def test_multiple_pizzas_add_up_correctly_order_2():
    """
    GIVEN a second order with different pizzas
    WHEN both pizzas are added
    THEN the total cost should be the correct sum
    """
    pizza1 = Pizza("Gluten Free", "Marinara", "Mozzarella", ["Pineapple"])
    pizza2 = Pizza("Thin", "Liv Sauce", "Mozzarella", ["Mushrooms", "Pepperoni"])
    order = Order()
    order.pizzas.append(pizza1)
    order.pizzas.append(pizza2)
    order.total += pizza1.cost_value + pizza2.cost_value

    expected_total = pizza1.cost_value + pizza2.cost_value
    assert len(order.pizzas) == 2
    assert order.total == expected_total

