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
        item_removed = False
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                item_removed = True
                break
        if item_removed == False:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
        # If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
        # If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
        item_found = False
        for item in self.cart_items:
            if item.name == ItemToPurchase.name:
                item_found = True
                if ItemToPurchase.description != "none":
                    item.description = ItemToPurchase.description
                if ItemToPurchase.price != 0:
                    item.price = ItemToPurchase.price
                if ItemToPurchase.quantity != 0:
                    item.quantity = ItemToPurchase.quantity
        if item_found == False:
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
        print("OUTPUT SHOPPING CART")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.date))
            print("Number of Items: {}".format(self.get_num_items_in_cart()))
            for item in self.cart_items:
                # print("{} {} @ ${:.2f} = ${:.2f}".format(item.name, item.quantity, item.price, item.price * item.quantity))
                item.print_item_cost()
            print("Total: ${:.2f}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        # Outputs each item's description.
        print("OUTPUT ITEMS' DESCRIPTIONS")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.date))
            print("Item Descriptions")
            for item in self.cart_items:
                print("{}: {}".format(item.name, item.description))