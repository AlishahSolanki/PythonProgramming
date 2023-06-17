inventory = {'apples': 105, 'bananas': 56, 'oranges': 0}

print('Current fruit inventory: ', inventory)

print('Enter latest fruit shipment received: ', end='')
fruit = input()

print('Enter quantity of {}: '.format(fruit), end='')
quantity = int(input())

# add fruit:quantity to dictionary
if (fruit in inventory):
    inventory[fruit] += quantity
    print('Amount of {} in store = {}'.format(fruit, inventory[fruit]))
else: # need add fruit to inventory
    inventory[fruit] = quantity

print(inventory.items())

print('Enter fruit being discontinued at store: ', end='')
fruit = input()

# delete fruit from dictionary
if (fruit in inventory):
    del inventory[fruit]
    print(fruit, 'no longer carried in store')
else: # fruit already not carried in store
    print(fruit, 'already not carried in store')

print('Total types of fruit in store =', len(inventory))
