'''
Build the ShoppingCart class with the following data attributes and related methods. Note: Some can be method stubs (empty methods) initially, to be completed in later steps

Parameterized constructor, which takes the customer name and date as parameters
Attributes
customer_name (string) - Initialized in default constructor to "none"
current_date (string) - Initialized in default constructor to "January 1, 2020"
cart_items (list)
Methods
add_item()
Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
remove_item()
Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
If item name cannot be found, output this message: Item not found in cart. Nothing removed.
modify_item()
Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
get_num_items_in_cart()
Returns quantity of all items in cart. Has no parameters.
get_cost_of_cart()
Determines and returns the total cost of items in cart. Has no parameters.
print_total()
Outputs total of objects in cart.
If cart is empty, output this message: SHOPPING CART IS EMPTY
print_descriptions()
Outputs each item's description.
Example of print_total() output:
John Doe's Shopping Cart - February 1, 2020
Number of Items: 8
Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128
Total: $521

Example of print_descriptions() output:
John Doe's Shopping Cart - February 1, 2020
Item Descriptions
Nike Romaleos: Volt color, Weightlifting shoes
Chocolate Chips: Semi-sweet
Powerbeats 2 Headphones: Bluetooth headphones


Implement Output shopping cart menu option. Implement Output item's description menu option.

Example of shopping cart menu option:
OUTPUT SHOPPING CART
John Doe's Shopping Cart - February 1, 2020
Number of Items: 8
Nike Romaleos 2 @ $189 = $378
Chocolate Chips 5 @ $3 = $15
Powerbeats 2 Headphones 1 @ $128 = $128
Total: $521

Example of item description menu option.
OUTPUT ITEMS' DESCRIPTIONS
John Doe's Shopping Cart - February 1, 2020
Item Descriptions
Nike Romaleos: Volt color, Weightlifting shoes
Chocolate Chips: Semi-sweet
Powerbeats 2 Headphones: Bluetooth headphones

'''

class ShoppingCart:
    def __init__(self, customer_name = "none", date = "January 1, 2020"):
        self.customer_name = customer_name
        self.date = date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        # Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
        self.cart_items.append(ItemToPurchase)

    def get_item(self, item_name):
        # Retrieves an item by name from cart.
        for item in self.cart_items:
            if item.name == item_name:
                return item
            else:
                print("Item not found in cart. Nothing modified.")

    def remove_item(self, item_name):
        # Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
        # If item name cannot be found, output this message: Item not found in cart. Nothing removed.
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                break
            else:
                print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
        # If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
        # If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
        for item in self.cart_items:
            if item.name == ItemToPurchase.name:
                if ItemToPurchase.description != "none":
                    item.description = ItemToPurchase.description
                if ItemToPurchase.price != 0:
                    item.price = ItemToPurchase.price
                if ItemToPurchase.quantity != 0:
                    item.quantity = ItemToPurchase.quantity
            else:
                print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        # Returns quantity of all items in cart. Has no parameters.
        return len(self.cart_items)

    def get_cost_of_cart(self):
        # Determines and returns the total cost of items in cart. Has no parameters.
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.price * item.quantity
        return total_cost

    def print_total(self):
        # Outputs total of objects in cart.
        # If cart is empty, output this message: SHOPPING CART IS EMPTY
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.date))
            print("Number of Items: {}".format(self.get_num_items_in_cart()))
            for item in self.cart_items:
                print("{} {} @ ${:.2f} = ${:.2f}".format(item.name, item.quantity, item.price, item.price * item.quantity))
            print("Total: ${}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        # Outputs each item's description.
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.date))
            print("Item Descriptions")
            for item in self.cart_items:
                print("{}: {}".format(item.name, item.description))