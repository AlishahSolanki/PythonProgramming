'''
Grading Rubric: 25 points total
   1 pt : comment with EUID
   1 pt : import random
   2 pts: prompt for (1 pt) and read in (1 pt) a single word
 1.5 pts: create set from word (1 pt), assign to my_set (0.5 pts)
   2 pts: if length of word ==  length of my_set, logic may be reversed
 0.5 pts: -- print contains no duplicate letters
   1 pt : else:
 0.5 pts: -- print contains duplicate letters
 2.5 pts: random number generation (2 pts), assignment to num (0.5 pts)
 1.5 pts: convert to letter (1 pt), assign to mystery (0.5 pts)
   2 pts: if mystery in my_set (logic may be reversed)
   2 pts: -- remove mystery from my_set
   1 pt : else
   2 pts: -- add mystery to my_set
   2 pts: create set with literal elements
   2 pts: find set difference
 0.5 pts: print set difference
'''

#EUID

import random

word = input('Enter a single word: ')

my_set = set(word)

if len(word) == len(my_set):
    print(word, 'contains no duplicate letters')
else:
    print(word, 'contains duplicate letters')

num = random.randint(97, 122)
mystery = chr(num)

if mystery in my_set:
    my_set.remove(mystery)
else:
    my_set.add(mystery)

new_set = {'a', 'e', 'i', 'o', 'u'}
#my_set.difference(new_set)
print(my_set.difference(new_set))
#print('difference =', my_set)
