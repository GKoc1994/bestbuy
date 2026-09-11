# Best Buy

A small command line store engine written with object-oriented Python. You can list the products, see how many items are in stock and place an order.

## Files

    products.py   Product class (price, quantity, active state, buying)
    store.py      Store class (holds products, total quantity, orders)
    main.py       Menu-based user interface

## Run it

    python3 main.py

## Behaviour

- Products with invalid details (empty name, negative price or quantity) raise a `ValueError`.
- Buying more than is in stock, buying from an inactive product or buying an invalid amount raises a `ValueError`.
- A product that runs out of stock is deactivated and no longer listed.
- An order is checked as a whole first, so nothing is bought if one item cannot be ordered.
