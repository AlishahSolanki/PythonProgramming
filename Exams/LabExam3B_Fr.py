'''
Grading Rubric: 18.5 points total (6.5 points in LabExam3BMOD_Fr.py)
   1 pt : import other Python module
   1 pt : create dictionary with two entries
 0.5 pts: print current homes on market message
   2 pts: iterate through dictionary to print the keys (names of homes)
 0.5 pts: prompt for and read in number new homes to add as an integer
   2 pts: call home_prices from imported module with number of new homes, assigning result
   1 pt : print price list returned from function call
   1 pt : use a loop for number of new homes to add
 0.5 pts: -- prompt for and read in name of new home on market
   2 pts: -- add new home keys with value from price list
   2 pts: iterate through dictionary to print keys and values separately
 0.5 pts: prompt for and read in name of home to buy (remove from market)
   1 pt : if home found in dictionary
 0.5 pts: -- print removing from market message
   1 pt : -- delete item from dictionary
 0.5 pts: else not in dictionary
 0.5 pts: -- print not available message
   1 pt : print dictionary
'''

import LabExam3BMOD_Fr

# EUID

real_estate = {'Hickory Street': 325800, 'Lawther Drive': 692848}

print('Current homes on the market: ', end='')
for house in real_estate.keys():
    print(house, end=' ')
print()

number = int(input('Enter number of new homes to go on the market: '))

price_list = LabExam3BMOD_Fr.home_prices(number)

print(price_list)

for i in range(number):
    new_home = input('Enter street name of new home on market: ')
    real_estate[new_home] = price_list[i]

for house, price in real_estate.items():
    print('{} : ${:.2f}'.format(house, price))

purchase = input('Enter the street name of the home you wish to buy: ')

if purchase in real_estate:
    print(purchase, 'home removed from market')
    real_estate.pop(purchase)
else:
    print(purchase, 'home not available')

print(real_estate)
