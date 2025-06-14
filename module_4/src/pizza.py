"""
pizza.py

Defines the Pizza class used in the pizza ordering system.
"""

# Cost lookup dictionaries
CRUST_PRICES = {
    "Thin": 5,
    "Thick": 6,
    "Gluten Free": 8
}

SAUCE_PRICES = {
    "Marinara": 2,
    "Pesto": 3,
    "Liv Sauce": 5
}

TOPPING_PRICES = {
    "Pineapple": 1,
    "Pepperoni": 2,
    "Mushrooms": 3
}

CHEESE_COST = 1


class Pizza:
    """
    Represents a customizable pizza and calculates its total cost.

    Requirements
    ------------
    - Exactly one crust
    - Exactly one sauce
    - One cheese (Mozzarella only)
    - At least one topping

    Cost Formula
    ------------
    Total = crust + sauce + cheese (fixed) + toppings
    """

    def __init__(self, crust, sauce, cheese, toppings):
        """
        Initialize a Pizza object with valid ingredients.

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

        :raises ValueError: If crust is not one of the allowed types.
        :raises ValueError: If sauce is not one of the allowed types.
        :raises ValueError: If toppings list is empty or contains invalid items.
        :raises ValueError: If cheese is not 'Mozzarella'.
        """
        if crust not in CRUST_PRICES:
            raise ValueError(f"Invalid crust: {crust}")
        if sauce not in SAUCE_PRICES:
            raise ValueError(f"Invalid sauce: {sauce}")
        if not toppings or any(t not in TOPPING_PRICES for t in toppings):
            raise ValueError(f"Invalid or missing toppings: {toppings}")
        if cheese.lower() != "mozzarella":
            raise ValueError(f"Only 'Mozzarella' cheese is allowed, got: {cheese}")

        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings
        self.cost_value = self.cost()

    def __str__(self):
        """
        Return a string representation of the pizza and its cost.

        :return: Summary of pizza combination and price
        :rtype: str
        """
        return (
            f"{self.crust} crust with {self.sauce} sauce, "
            f"{self.cheese} cheese, toppings: {', '.join(self.toppings)} - "
            f"${self.cost_value:.2f}"
        )

    def cost(self):
        """
        Compute the total cost of the pizza based on the ingredients.

        :return: Total cost of pizza in dollars
        :rtype: float
        """
        crust_cost = CRUST_PRICES[self.crust]
        sauce_cost = SAUCE_PRICES[self.sauce]
        topping_cost = sum(TOPPING_PRICES[t] for t in self.toppings)
        return crust_cost + sauce_cost + CHEESE_COST + topping_cost
