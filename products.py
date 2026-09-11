"""Product class for the Best Buy store."""


class Product:
    """A product in the store with a name, a price and a quantity in stock."""

    def __init__(self, name, price, quantity):
        """Create a product. Raise ValueError if the details are invalid."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name cannot be empty.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price cannot be negative.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Return the quantity in stock."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the quantity in stock. A product with 0 left is deactivated."""
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Return True if the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def __str__(self):
        """Return a string that describes the product."""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def show(self):
        """Print a string that represents the product."""
        print(self)

    def buy(self, quantity):
        """Buy the given quantity and return the total price.

        Raise an exception if the quantity is invalid, the product is
        inactive or there is not enough in stock.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Invalid Quantity")
        if not self.active:
            raise ValueError("Product Inactive")
        if quantity > self.quantity:
            raise ValueError("Quantity larger than what exists")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price
