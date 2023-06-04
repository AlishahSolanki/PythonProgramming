'''
Grading Rubric: 25 points total
   1 pt : comment with EUID
   3 pts: create dictionary with two keys-values
   2 pts: promot for (1 pt), read in (1 pt) name of fruit to add
   2 pts: prompt for (1 pt), read in price per pound as float (1 pt)
   2 pts: add fruit and price per pound to price_list
   2 pts: print price_list with keys-values
   2 pts: prompt for (1 pt), read in (1 pt) name of fruit wish to purchase
   2 pts: prompt for (1 pt), read in number of pounds as integer (1 pt)
   2 pts: if fruit in price_list (logic may be reversed)
   3 pts: -- compute total using price_list and pounds (2 pts), assign to total (1 pt)
   2 pts: -- print message with pounds, fruit, total (1 pt), formatted two decimal places (1 pt)
   1 pt : else 
   1 pt : -- print out of stock message
'''

#EUID

price_list = {'bananas': 0.58, 'apples': 1.69}

fruit = input('Enter name of fruit to add: ')
price = float(input('Enter price per pound: '))

price_list[fruit] = price

print(price_list)

name = input('Enter name of fruit you wish to purchase: ')
pounds = int(input('Enter number of pounds you wish to buy: '))

if name in price_list:
    total = price_list[name] * pounds
    print('{} pounds of {} totals ${:.2f}'.format(pounds, name, total))
else:
    print(name, 'out of stock')
