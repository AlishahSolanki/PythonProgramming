'''
Grading Rubric: 25 points total
 0.5 pts: comment with EUID
   4 pts: function definition: syntax/name (2 pt), parameters (1 pt), default values (1 pt)
 1.5 pts: -- iterate through list
   1 pt : -- -- convert to character
   1 pt : -- -- if alphabetic or numeric
   1 pt : -- -- -- add character to string
   1 pt : -- -- else if space
   1 pt : -- -- -- add space argument to string
   1 pt : -- -- else (not alphanumeric or space)
   1 pt : -- -- -- print discard message with character
   1 pt : -- print secret message
 1.5 pts: loop: init (0.5 pts), condition (0.5 pts), update (0.5 pts)
   1 pt : -- generate random number between 32 and 126
 1.5 pts: -- add random number to list
   1 pt : print list
   1 pt : prompt for (0.5 pts), read in Y/N to enter space value (0.5 pts)
   1 pt : if response == 'Y'
   1 pt : -- prompt for (0.5 pts), read in single replacement character (0.5 pts)
   1 pt : -- function call (0.5 pts), arguments (0.5 pts)
   1 pt : else (anything other than 'Y')
   1 pt : -- function call (0.5 pts), arguments (0.5 pts)
'''

#EUID

import random

def secret_message(my_list, space = '-'):
    new_str = ''
    for value in my_list:
        ch = chr(value)
        if ch.isalnum():
            new_str += ch
        elif ch.isspace():
            new_str += space
        else:
            print('Discarding', ch)
    print('Secret message:', new_str)

my_list = []
count = 0

while count < 10:
    x = random.randint(32, 126)
    my_list.append(x)
    count += 1

print(my_list)

response = input('Do you want to enter a value for space character? (Y/N) ')

if response == 'Y':
    ch = input('Enter a single character: ')
    secret_message(my_list, ch[0])
else:
    secret_message(my_list)

