'''
Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
The program should first ask for the number of years. The outer loop will iterate once for each year. 
The inner loop will iterate twelve times, once for each month. 
Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.
'''

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print('Enter the number of years of rainfall data: ', end = '')
num_years = int(input())
total_inches = 0
for year in range(num_years):
    for month in range(12):
        print('Enter the inches of rainfall for', months[month], 'of year', year + 1, ': ', end = '')
        inches = float(input())
        total_inches += inches

average = total_inches / (num_years * 12)
print('Number of months: ', num_years * 12)
print('Total inches of rainfall: ', total_inches)
print('Average monthly rainfall: ', average)