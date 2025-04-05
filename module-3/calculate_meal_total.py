'''
Write a program that calculates the total amount of a meal purchased at a restaurant. 
The program should ask the user to enter the charge for the food and then calculate 
the amounts with an 18 percent tip and 7 percent sales tax. 
Display each of these amounts and the total price.
'''

print('Enter the total charge for the meal: ', end = ' ')
charge = float(input())
if charge > 0:
    tip = round(charge * 0.18, 2)
    sales_tax = round(charge * 0.07, 2)
    total = round(charge + tip + sales_tax, 2)
    print('Tip:', '${0:.2f}'.format(tip))
    print('Sales tax:', '${0:.2f}'.format(sales_tax))
    print('Total:', '${0:.2f}'.format(total))
else:
    print('Amount must be a positive number.')