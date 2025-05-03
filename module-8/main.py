from order_class import ItemToPurchase
from shopping_cart import ShoppingCart

def print_menu(cart):
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")    
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print("Choose an option:")

print("Enter customer's name:")
name = str(input())
print("Enter today's date:")
date = str(input())
cart = ShoppingCart(name, date)
cart.print_customer_date()
print("\n")

print_menu(cart)
user_input = str(input())
while(user_input != "q"):
    if(user_input == "a"):
        print("ADD ITEM TO CART")
        print("Enter the item name:")
        item_name = str(input())
        print("Enter the item description:")
        item_desc = str(input())
        print("Enter the item price:")
        item_price = float(input())
        print("Enter the item quantity:")
        item_qty = int(input())

        newItem = ItemToPurchase()
        newItem.name = item_name
        newItem.price = item_price
        newItem.quantity = item_qty
        newItem.description = item_desc
        newItem1Total = newItem.price * newItem.quantity
        cart.add_item(newItem)
    elif(user_input == "r"):
        print("REMOVE ITEM FROM CART")
        print("Enter name of item to remove:")
        item_name = str(input())
        cart.remove_item(item_name)
    elif(user_input == "c"):
        print("CHANGE ITEM QUANTITY")
        print("Enter the item name:")
        item_name = str(input())
        item = cart.get_item(item_name)

        if item != None:
            print("Enter updated quantity:")
            new_quantity = int(input())
            item.quantity = new_quantity
            cart.modify_item(item)
    elif(user_input == "i"):
        cart.print_descriptions()
    elif(user_input == "o"):
        cart.print_total()
    
    print_menu(cart)
    user_input = str(input())