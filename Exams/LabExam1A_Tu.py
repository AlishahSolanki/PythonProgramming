'''
Grading Rubric: 25 points total
   1 pt : comment with EUID
   1 pt : import collections (for namedtuple)
   1 pt : import math
   1 pt : import random
   3 pts: define RightTriangle namedtuple: assignment (1 pt), function (1 pt), parameters (1 pt)
   2 pts: prompt for (1 pt) read in length of leg a as float (1 pt)
   2 pts: if a > 0 (logic may be reversed)
   3 pts: -- random number generation (2 pts), assignment to b (1 pt)
   3 pts: -- compute sqrt (1 pt), sqrt parameters (1 pt), assignment to c (1 pt)
   3 pts: -- create my_triangle namedtuple (2 pts), parameters (1 pt)
   3 pts: -- print my_triangle (1 pt), using namedtuple fields (1 pt), formatted 2 decimal places (1 pt)
   1 pt : else
   1 pt : -- print error message
'''

#EUID

from collections import namedtuple
import math
import random

RightTriangle = namedtuple('RightTriangle', ['a', 'b', 'c'])

a = float(input('Enter length of leg \'a\' of right triangle: '))

if a > 0:
    b = random.randint(5, 10)
    c = math.sqrt(pow(a, 2) + pow(b, 2))
    my_triangle = RightTriangle(a, b, c)

    print('my_triangle: a={:.2f} b={:.2f} c={:.2f}'.format(my_triangle.a, my_triangle.b, my_triangle.c))
else:
    print('Error: leg \'a\' must be positive')

