'''
Grading Rubric: 6.5 points total
 0.5 pts: import random
   ------ function definition
 0.5 pts: definition syntax
 0.5 pts: create empty list
 0.5 pts: initialize (seed) random number generator
   1 pt : using a loop, generate random number and append to list
 0.5 pts: return list
   ------ main
   1 pts: if __name__ == '__main__':
 0.5 pts: -- prompt for and read in number items in list
   1 pt : -- call stock_inventory function, passing number, assign return value to list
 0.5 pts: -- print list
'''

import random

def home_prices(number):
    price_list = []
    random.seed()
    for i in range(number):
        price_list.append(random.randint(100000, 500000))
    return price_list

if __name__ == '__main__':
    number = int(input('Enter number of homes going on the market: '))
    my_list = home_prices(number)
    print(my_list)

