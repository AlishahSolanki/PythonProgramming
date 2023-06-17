import random

print('Enter a string (>1 character) to be encrypted: ', end='')
str1 = input()

# convert string to list
list1 = []
list1[:0] = str1

print('Original list:', list1)

# append random lowercase letter (a=97 to z=122)
num = random.randint(97, 122)
list1.append(chr(num))

# append first two characters to end of list
list2 = list1[:2] # list of first two characters
list1 = list1 + list2

# remove first two characters from list
list1.remove(str1[0])
list1.remove(str1[1])

print('Encrypted list:', list1)

# convert list to string and print encrypted string
str2 = ""
str2 = str2.join(list1)
print('Encrypted string:', str2)
