"""Unit tests for the Product class."""
import pytest

import promotions
from products import LimitedProduct, NonStockedProduct, Product


def test_creating_prod():
    """Creating a normal product works."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.get_quantity() == 100
    assert product.is_active()


def test_creating_prod_invalid_details():
    """Invalid details (empty name, negative price) raise an exception."""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=1450, quantity=-5)


def test_prod_becomes_inactive():
    """A product that reaches 0 quantity becomes inactive."""
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)
    assert product.get_quantity() == 0
    assert not product.is_active()

    other = Product("Google Pixel 7", price=500, quantity=250)
    other.set_quantity(0)
    assert not other.is_active()


def test_buy_modifies_quantity():
    """Buying reduces the quantity and returns the total price."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.buy(3) == 4350
    assert product.get_quantity() == 97


def test_buy_too_much():
    """Buying more than exists raises an exception."""
    product = Product("MacBook Air M2", price=1450, quantity=10)
    with pytest.raises(ValueError):
        product.buy(11)
    assert product.get_quantity() == 10


def test_non_stocked_product():
    """A non stocked product can always be bought and keeps quantity 0."""
    product = NonStockedProduct("Windows License", price=125)
    assert product.buy(1000) == 125000
    assert product.get_quantity() == 0
    assert product.is_active()


def test_limited_product():
    """A limited product refuses orders above its maximum."""
    product = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    assert product.buy(1) == 10
    with pytest.raises(ValueError):
        product.buy(2)
    assert product.get_quantity() == 249


def test_promotions():
    """Every promotion calculates the right total price."""
    product = Product("Google Pixel 7", price=500, quantity=250)
    product.set_promotion(promotions.PercentDiscount("30% off!", percent=30))
    assert product.buy(2) == 700
    product.set_promotion(promotions.SecondHalfPrice("Second Half price!"))
    assert product.buy(3) == 1250
    product.set_promotion(promotions.ThirdOneFree("Third One Free!"))
    assert product.buy(3) == 1000
    assert product.get_quantity() == 242
