'''
In the main section of your code, implement the print_menu() function. print_menu() has a ShoppingCart parameter and outputs a menu of options to manipulate the shopping cart. Each option is represented by a single character. Build and output the menu within the function.

If an invalid character is entered, continue to prompt for a valid choice. Hint: Implement Quit before implementing other options. Call print_menu() in the main() function. Continue to execute the menu until the user enters q to Quit.
Example:
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option:
'''

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

cart = ShoppingCart("John Doe", "February 1, 2020")
print_menu(cart)
user_input = str(input())
while(user_input != "q"):
    if(user_input == "a"):
        print("Enter the item name:")
        item_name = str(input())
        print("Enter the item price:")
        item_price = float(input())
        print("Enter the item quantity:")
        item_qty = int(input())
        print("Enter the item description:")
        item_desc = str(input())

        newItem = ItemToPurchase()
        newItem.name = item_name
        newItem.price = item_price
        newItem.quantity = item_qty
        newItem.description = item_desc
        newItem1Total = newItem.price * newItem.quantity
        cart.add_item(newItem)
    elif(user_input == "r"):
        print("Enter the item name:")
        item_name = str(input())
        cart.remove_item(item_name)
    elif(user_input == "c"):
        print("Enter the item name:")
        item_name = str(input())
        item = cart.get_item(item_name)

        if item != None:
            cart.modify_item(item)
    elif(user_input == "i"):
        cart.print_descriptions()
    elif(user_input == "o"):
        cart.print_total()
    
    print("Choose an option:")
    user_input = str(input())