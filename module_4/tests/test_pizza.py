"""
Unit tests for the Pizza class.
"""

import pytest
from src.pizza import Pizza, CRUST_PRICES, SAUCE_PRICES, TOPPING_PRICES, CHEESE_COST


@pytest.mark.pizza
def test_pizza__init__():
    """
    GIVEN valid ingredients
    WHEN a Pizza object is initialized
    THEN it should return an initialized Pizza instance with expected attributes
    """
    pizza = Pizza("Thin", "Marinara", "Mozzarella", ["Pepperoni"])
    assert pizza.crust == "Thin"
    assert pizza.sauce == "Marinara"
    assert pizza.cheese == "Mozzarella"
    assert pizza.toppings == ["Pepperoni"]

@pytest.mark.pizza
def test_pizza_attributes():
    """
    GIVEN a valid Pizza
    WHEN it is initialized
    THEN the attributes should match expected types
    """
    pizza = Pizza("Thick", "Pesto", "Mozzarella", ["Mushrooms"])
    assert isinstance(pizza.crust, str)
    assert isinstance(pizza.sauce, str)
    assert isinstance(pizza.cheese, str)
    assert isinstance(pizza.toppings, list)

@pytest.mark.pizza
def test_pizza_cost_non_zero():
    """
    GIVEN a valid pizza
    WHEN the cost is computed
    THEN the value should be greater than 0
    """
    pizza = Pizza("Gluten Free", "Liv Sauce", "Mozzarella", ["Pepperoni"])
    assert pizza.cost_value > 0

@pytest.mark.pizza
def test_pizza__str__():
    """
    GIVEN a pizza
    WHEN str() is called
    THEN it should return a string with description and price
    """
    pizza = Pizza("Thin", "Marinara", "Mozzarella", ["Pepperoni"])
    result = str(pizza)
    assert "Thin" in result
    assert "Marinara" in result
    assert "Mozzarella" in result
    assert "Pepperoni" in result
    assert f"${pizza.cost_value:.2f}" in result

@pytest.mark.pizza
def test_pizza_cost():
    """
    GIVEN specific ingredients
    WHEN a pizza is created
    THEN cost() should return the expected total
    """
    crust = "Thick"
    sauce = "Pesto"
    toppings = ["Pineapple", "Pepperoni"]
    expected = (
        CRUST_PRICES[crust]
        + SAUCE_PRICES[sauce]
        + CHEESE_COST
        + sum(TOPPING_PRICES[t] for t in toppings)
    )
    pizza = Pizza(crust, sauce, "Mozzarella", toppings)
    assert pizza.cost_value == expected
