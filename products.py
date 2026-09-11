"""Product classes for the Best Buy store."""


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
        self.promotion = None

    @property
    def price(self):
        """The price of one item."""
        return self._price

    @price.setter
    def price(self, price):
        """Set the price. Raise ValueError if it is negative."""
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = price

    def __gt__(self, other):
        """Return True if this product is more expensive than `other`."""
        return self.price > other.price

    def __lt__(self, other):
        """Return True if this product is cheaper than `other`."""
        return self.price < other.price

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

    def get_promotion(self):
        """Return the current promotion, or None."""
        return self.promotion

    def set_promotion(self, promotion):
        """Set the current promotion. Use None to remove it."""
        self.promotion = promotion

    def get_promotion_name(self):
        """Return the name of the current promotion, or 'None'."""
        return self.promotion.name if self.promotion else "None"

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
        return (f"{self.name}, Price: ${self.price}, "
                f"Quantity: {self.quantity}, "
                f"Promotion: {self.get_promotion_name()}")

    def show(self):
        """Print a string that represents the product."""
        print(self)

    def validate_purchase(self, quantity):
        """Raise ValueError if the given quantity cannot be bought."""
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Invalid Quantity")
        if not self.active:
            raise ValueError("Product Inactive")
        if quantity > self.quantity:
            raise ValueError("Quantity larger than what exists")

    def get_total_price(self, quantity):
        """Return the price for `quantity` items, using the promotion."""
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def buy(self, quantity):
        """Buy the given quantity and return the total price.

        Raise ValueError if the quantity is invalid, the product is
        inactive or there is not enough in stock.
        """
        self.validate_purchase(quantity)
        total_price = self.get_total_price(quantity)
        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    """A product that is not physical, so its quantity is not tracked."""

    def __init__(self, name, price):
        """Create a non stocked product. Its quantity is always 0."""
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        """Keep the quantity at 0, a non stocked product has no stock."""

    def validate_purchase(self, quantity):
        """Raise ValueError if the quantity is invalid or it is inactive."""
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Invalid Quantity")
        if not self.active:
            raise ValueError("Product Inactive")

    def buy(self, quantity):
        """Buy any amount and return the total price."""
        self.validate_purchase(quantity)
        return self.get_total_price(quantity)

    def __str__(self):
        """Return a string that describes the product."""
        return (f"{self.name}, Price: ${self.price}, Quantity: Unlimited, "
                f"Promotion: {self.get_promotion_name()}")


class LimitedProduct(Product):
    """A product that can only be bought a limited amount per order."""

    def __init__(self, name, price, quantity, maximum):
        """Create a product that allows at most `maximum` items per order."""
        super().__init__(name, price, quantity)
        if not isinstance(maximum, int) or maximum < 1:
            raise ValueError("Maximum must be a positive whole number.")
        self.maximum = maximum

    def validate_purchase(self, quantity):
        """Also refuse orders that are larger than the allowed maximum."""
        super().validate_purchase(quantity)
        if quantity > self.maximum:
            raise ValueError(
                f"Only {self.maximum} is allowed from this product!")

    def __str__(self):
        """Return a string that describes the product."""
        return (f"{self.name}, Price: ${self.price}, "
                f"Limited to {self.maximum} per order!, "
                f"Promotion: {self.get_promotion_name()}")
