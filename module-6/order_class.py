class ItemToPurchase:
    def __init__(self):
        self.name = "none"
        self.price = 0
        self.quantity = 0
        self.description = ""

    def print_item_cost(self):
        # Print item cost, remove decimals when they are unnecessary
        if self.price == int(self.price):
            print('{} {} @ ${} = ${}'.format(self.name, self.quantity, int(self.price), int(self.price) * self.quantity))
        else:
            print('{} {} @ ${:.2f} = ${:.2f}'.format(self.name, self.quantity, self.price, self.price * self.quantity))