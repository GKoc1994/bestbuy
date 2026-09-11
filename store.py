"""Store class that holds the products of the Best Buy store."""


class Store:
    """A store with a list of products."""

    def __init__(self, products):
        """Create a store with the given list of products."""
        self.products = list(products)

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """Return how many items are in the store in total."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """Return a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """Buy all (product, quantity) pairs and return the total price.

        The whole order is checked first, so nothing is bought if any
        item cannot be ordered.
        """
        requested = {}
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"{product.name} is not sold in this store")
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("Invalid Quantity")
            requested[product] = requested.get(product, 0) + quantity

        for product, quantity in requested.items():
            product.validate_purchase(quantity)

        return sum(product.buy(quantity)
                   for product, quantity in shopping_list)
