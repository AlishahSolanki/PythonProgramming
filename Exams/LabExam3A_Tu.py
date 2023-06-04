'''
Grading Rubric: 25 points total
 0.5 pts: import sys
   ------ SideException class definition
   2 pts: definition syntax
   ------ RegPoly class definition
   1 pt : definition syntax
   2 pts: __init__ constructor definition (1 pt), parameters (1 pt, 0.5 pts each)
   1 pt : -- assign parameter to sides instance variable
   2 pts: -- compute internal angle (1 pt), assign to angle instance variable
   2 pts: __str__ method definition (1 pt), parameter (1 pt)
   2 pts: string construction (1 pt), return (1 pt)
   ------ main
   2 pts: loop over command-line arguments
 0.5 pts: -- try:
   1 pt : -- -- check for invalid number of sides (i.e., < 3)
   2 pts: -- -- -- raise SideException (1 pt), error message (1 pt)
   1 pt : -- except SideException as error message:
   1 pt : -- -- print error message with detail
 0.5 pts: -- else:
   2 pts: -- -- instantiate RegPoly object (1 pt) with argument (0.5 pts), assignment (0.5 pts)
   1 pt : -- -- print object, which invokes __str__ method
   1 pt : -- finally:
 0.5 pts: -- -- increment counter for loop
'''

import sys

class SideException(Exception):
    pass

class RegPoly:
    def __init__(self, numSides):
        self.sides = numSides
        self.angle = (self.sides - 2) * 180 / self.sides
    def __str__(self):
        return 'sides=' + str(self.sides) + ', internal angles=' + str(self.angle)

i = 1

while i < len(sys.argv):
    try:
        if int(sys.argv[i]) < 3: # invalid regular polygon
            raise SideException('Invalid number of sides for regular polygon: ' + sys.argv[i])
    except SideException as errmsg:
        print('SideException:', errmsg)
    else:
        my_poly = RegPoly(int(sys.argv[i]))
        print(my_poly)
    finally:
        i += 1

