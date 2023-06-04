def print_list(list_to_print):
    for i in range(len(list_to_print)):
        print('{:2}'.format(list_to_print[i]), end=' ')
    print()

def print_2D_list(list_2D_to_print):
    for i in range(len(list_2D_to_print)):
        print_list(list_2D_to_print[i])

v = 0
two_d = []            # create an empty list
for i in range(5):
    two_d.append([])  # append an empty list to two_d
    for j in range(4):
        two_d[i].append(v)   # two_d[i] is the empty list that we just created.
                             # here, we are adding elements to it.
        v += 1 

print_2D_list(two_d)
print()

new_2d = [[(i * 2) for i in row] for row in two_d]

print_2D_list(new_2d)

