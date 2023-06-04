'''
Grading Rubric: 25 points total
 0.5 pts: comment with EUID
   4 pts: function definition: syntax/name (1 pt), parameters (1 pt), default values (1 pt)
   3 pts: -- loop (1.5 pts), range (1.5 pts), partial points
 1.5 pts: -- -- add numbers to list (many ways to do)
   2 pts: -- return list
   1 pt : prompt for (0.5 pts), read in stop value as integer (0.5 pts)
   1 pt : prompt for (0.5 pts), read in Y/N to enter start value (0.5 pts)
 1.5 pts: if statement (0.5 pts), 'Y' or 'y' (0.5 pts), first character of string (0.5 pts)
   1 pt : -- prompt for (0.5 pts), read in start value as integer (0.5 pts)
   1 pt : -- prompt for (0.5 pts), read in Y/N to enter step value (0.5 pts)
 1.5 pts: -- if statement (0.5 pts), 'Y' or 'y' (0.5 pts), first character of string (0.5 pts)
   1 pt : -- -- prompt for (0.5 pts), read in step value as integer (0.5 pts)
 1.5 pts: -- -- function call (0.5 pts), arguments (0.5 pts), assignment (0.5 pts)
 0.5 pts: -- else (not positive response for step value)
 1.5 pts: -- -- function call (0.5 pts), arguments (0.5 pts), assignment (0.5 pts)
 0.5 pts: else (not positive response for start value)
 1.5 pts: -- function call (0.5 pts), arguments (0.5 pts), assignment (0.5 pts)
 0.5 pts: print list
'''

#EUID

def create_list(stop, start = 0, step = 1):
    my_list = []
    for value in range(start, stop, step):
        my_list.append(value)
    return my_list

stop = int(input('Enter a stop value: '))

response = input('Do you want to enter a start value? (Y/N) ')
if response[0].upper() == 'Y':
    start = int(input('Enter a start value: '))

    response = input('Do you want to enter a step value? (Y/N) ')
    if response[0].upper() == 'Y':
        step = int(input('Enter a step value: '))
        my_list = create_list(stop, start, step)
    else:
        my_list = create_list(stop, start)
else:
    my_list = create_list(stop)

print(my_list)
