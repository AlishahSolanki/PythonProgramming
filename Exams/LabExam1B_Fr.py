'''
Grading Rubric: 25 points total
   1 pt : comment with EUID
   3 pts: create dictionary with three keys-values
   2 pts: prompt for (1 pt), read in (1 pt) name of stock to delete
 1.5 pts: if stock in stock_prices
   2 pts: -- delete stock from dictionary
   2 pts: prompt for (1 pt), read in (1 pt) name of stock to update
 1.5 pts: if stock in stock_prices (logic may be reversed)
   2 pts: -- retrieve current price of stock
   2 pts: -- compute loss as square root of current price
   2 pts: -- assign new price as current price - loss
   1 pt : else
   2 pts: -- prompt for (1 pt) and read in new price as float (1 pt)
   2 pts: -- assign new price to stock_prices
   1 pt : print stock_prices
'''

#EUID

import math

stock_prices = {'ABC': 5.17, 'XYZ': 2.38, 'PQR': 7.84}

stock = input('Enter name of stock to delete: ')

if stock in stock_prices:
    del stock_prices[stock]

stock = input('Enter name of stock to update price: ')

if stock in stock_prices:
    current_price = stock_prices[stock]
    loss = math.sqrt(current_price)
    stock_prices[stock] = current_price - loss
else:
    new_price = float(input('Enter price of new stock: '))
    stock_prices[stock] = new_price

print(stock_prices)




