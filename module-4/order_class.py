class ItemToPurchase:
    def __init__(self):
        self.name = "none"
        self.price = 0
        self.quantity = 0

    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.name, self.quantity, self.price, self.price * self.quantity))