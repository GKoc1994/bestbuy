"""Command line interface for the Best Buy store."""
import products
import store

MENU_OPTIONS = [
    "List all products in store",
    "Show total amount in store",
    "Make an order",
    "Quit",
]


def print_menu():
    """Print the store menu."""
    print("\n   Store Menu\n   ----------")
    for number, option in enumerate(MENU_OPTIONS, start=1):
        print(f"{number}. {option}")


def print_product_list(product_list):
    """Print the given products as a numbered list."""
    print("------")
    for number, product in enumerate(product_list, start=1):
        print(f"{number}. {product}")
    print("------")


def show_products(best_buy):
    """Print all active products of the store."""
    print_product_list(best_buy.get_all_products())


def show_total_amount(best_buy):
    """Print how many items are in the store in total."""
    print(f"Total of {best_buy.get_total_quantity()} items in store")


def make_order(best_buy):
    """Let the user pick products and amounts, then place the order."""
    product_list = best_buy.get_all_products()
    print_product_list(product_list)
    print("When you want to finish order, enter empty text.")

    shopping_list = []
    prompt = "Which product # do you want? "
    while True:
        product_choice = input(prompt).strip()
        amount_choice = input("What amount do you want? ").strip()
        prompt = "\nWhich product # do you want? "
        if not product_choice or not amount_choice:
            break
        try:
            product = product_list[int(product_choice) - 1]
            amount = int(amount_choice)
            if int(product_choice) < 1 or amount <= 0:
                raise ValueError
        except (ValueError, IndexError):
            print("Error adding product!")
            continue
        shopping_list.append((product, amount))
        print("Product added to list!")

    if not shopping_list:
        return
    try:
        total_payment = best_buy.order(shopping_list)
    except ValueError as error:
        print(f"Error while making order! {error}")
        return
    print(f"********\nOrder made! Total payment: ${total_payment}")


def start(best_buy):
    """Show the menu until the user quits."""
    actions = {
        "1": show_products,
        "2": show_total_amount,
        "3": make_order,
    }
    while True:
        print_menu()
        try:
            choice = input("Please choose a number: ").strip()
        except EOFError:
            break
        if choice == "4":
            break
        action = actions.get(choice)
        if action is None:
            print("Error with your choice! Try again!")
            continue
        try:
            action(best_buy)
        except EOFError:
            break


def main():
    """Create the initial stock and start the store."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
