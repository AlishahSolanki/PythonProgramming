import random
from datetime import datetime

def linear_search(numbers, key):
    for i in range(len(numbers)):
        if numbers[i] == key:
            return i
    return -1 # not found

def binary_search(numbers, key):
    low = 0
    high = len(numbers) - 1
    while high >= low:
        mid = (high + low) // 2
        if numbers[mid] < key:
            low = mid + 1
        elif numbers[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1 # not found

i = 0
my_list = []

while i < 10000000:
    my_list.append(random.randint(1, 100000000))
    i += 1

start_time = datetime.now()
print('Linear Search Results:', linear_search(my_list, -5))
end_time = datetime.now()
print('Linear Search Duration: {}'.format(end_time - start_time))

sorted(my_list)

start_time = datetime.now()
print('Binary Search Results:', binary_search(my_list, -5))
end_time = datetime.now()
print('Binary Search Duration: {}'.format(end_time - start_time))
