# Best Buy

A small command line store engine written with object-oriented Python. You can list the products, see how many items are in stock and place an order.

## Files

    products.py      Product, NonStockedProduct and LimitedProduct classes
    promotions.py    Promotion base class and the PercentDiscount,
                     SecondHalfPrice and ThirdOneFree promotions
    store.py         Store class (holds products, total quantity, orders)
    main.py          Menu-based user interface
    test_product.py  Unit tests (pytest)

## Run it

    python3 main.py

## Run the tests

    pytest test_product.py

## Behaviour

- Products with invalid details (empty name, negative price or quantity) raise a `ValueError`.
- Buying more than is in stock, buying from an inactive product or buying an invalid amount raises a `ValueError`.
- A product that runs out of stock is deactivated and no longer listed.
- A `NonStockedProduct` (e.g. a software license) has no stock, so any amount can be bought.
- A `LimitedProduct` (e.g. shipping) can only be bought up to a maximum amount per order.
- A product can have one promotion. The promotion is used to calculate the price when buying.
- An order is checked as a whole first, so nothing is bought if one item cannot be ordered.
- Products can be compared by price (`>` / `<`), `product in store` checks if a store sells a product and `store1 + store2` combines two stores.
