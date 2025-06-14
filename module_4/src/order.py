"""
order.py

Defines the Order class for customer pizza orders used in the pizza ordering system.
"""

from src.pizza import Pizza

class Order:
    """
    Represents a customer order containing one or more pizzas.

    Requirements
    ------------
    - Orders begin empty and unpaid
    - Each order must include at least one pizza
    - Each pizza is added using the `input_pizza()` method
    - The order must be explicitly marked as paid using `order_paid()`

    Behavior
    --------
    - Maintains a list of pizzas in the order
    - Calculates total cost by summing all pizza costs
    - Tracks whether the order has been paid

    Attributes
    ----------
    pizzas : list of Pizza
        List of pizzas added to the order
    total : float
        Total cost of the order
    paid : bool
        Indicates whether the order has been paid
    """


    def __init__(self):
        """
        Initialize a new empty order.

        Sets:
            self.pizzas to an empty list.
            self.total to 0.0.
            self.paid to False.
        """
        self.pizzas = []
        self.total = 0.0
        self.paid = False

    def __str__(self):
        """
        Return a full string summary of the order, including pizza details and total cost.

        :return: Multi-line string of the full order and its total cost.
        :rtype: str
        """
        order_summary = '\n'.join(str(pizza) for pizza in self.pizzas)
        return f"Order:\n{order_summary}\nTotal: ${self.total:.2f}"

    def input_pizza(self, crust, sauce, cheese, toppings):
        """
        Create a Pizza object and add it to the order.

        The pizza will be added to the order's list, and its cost added to the total.

        :param crust: Type of crust. Must be one of:
                      "Thin", "Thick", "Gluten Free"
        :type crust: str
        :param sauce: Type of sauce. Must be one of:
                      "Marinara", "Pesto", "Liv Sauce"
        :type sauce: str
        :param cheese: Type of cheese. Must be "Mozzarella" (case-insensitive).
        :type cheese: str
        :param toppings: List of toppings. Each must be one of:
                         "Pineapple", "Pepperoni", "Mushrooms"
        :type toppings: list[str]

        :raises ValueError: If any of the pizza parameters are invalid
                            (as raised by the Pizza class constructor).
        """
        pizza = Pizza(crust, sauce, cheese, toppings)
        self.pizzas.append(pizza)
        self.total += pizza.cost_value

    def order_paid(self):
        """
        Mark the order as paid by setting the `paid` attribute to True.
        """
        self.paid = True
