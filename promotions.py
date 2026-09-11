"""Promotions that can be applied to products of the Best Buy store."""
from abc import ABC, abstractmethod


class Promotion(ABC):
    """Base class for all promotions. A promotion has a name."""

    def __init__(self, name):
        """Create a promotion with the given name."""
        self.name = name

    def get_name(self):
        """Return the name of the promotion."""
        return self.name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Return the price for `quantity` items of `product` after the
        promotion was applied."""


class PercentDiscount(Promotion):
    """A discount of a fixed percentage on every item."""

    def __init__(self, name, percent):
        """Create a discount of `percent` percent (0 to 100)."""
        super().__init__(name)
        if not isinstance(percent, (int, float)) or not 0 <= percent <= 100:
            raise ValueError("Percent must be between 0 and 100.")
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """Return the total price with the percentage taken off."""
        return product.price * quantity * (100 - self.percent) / 100


class SecondHalfPrice(Promotion):
    """Every second item costs half price."""

    def apply_promotion(self, product, quantity):
        """Return the total price where every second item is half price."""
        half_price_items = quantity // 2
        full_price_items = quantity - half_price_items
        return (full_price_items * product.price
                + half_price_items * product.price / 2)


class ThirdOneFree(Promotion):
    """Buy 2, get the third one for free."""

    def apply_promotion(self, product, quantity):
        """Return the total price where every third item is free."""
        free_items = quantity // 3
        return (quantity - free_items) * product.price
