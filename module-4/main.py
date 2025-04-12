from order_class import ItemToPurchase

# Get first item's info
print("Item 1")
print("Enter the item name:")
item1_name = str(input())
print("Enter the item price:")
item1_price = int(input())
print("Enter the item quantity:")
item1_qty = int(input())

newItem1 = ItemToPurchase()
newItem1.name = item1_name
newItem1.price = item1_price
newItem1.quantity = item1_qty
newItem1Total = newItem1.price * newItem1.quantity

# Get second item's info
print("Item 2")
print("Enter the item name:")
item2_name = str(input())
print("Enter the item price:")
item2_price = int(input())
print("Enter the item quantity:")
item2_qty = int(input())

newItem2 = ItemToPurchase()
newItem2.name = item2_name
newItem2.price = item2_price
newItem2.quantity = item2_qty
newItem2Total = newItem2.price * newItem2.quantity

# Print final output
print('TOTAL COST')
newItem1.print_item_cost()
newItem2.print_item_cost()
print('Total: ${}'.format(newItem1Total + newItem2Total))