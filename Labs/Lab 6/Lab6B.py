def input_list():
    my_list = []
    n = int(input("Enter number of integers in list: "))
    for i in range(0, n):
        item = int(input('Enter item #{}: '.format(i + 1)))
        my_list.append(item)
    return my_list

def second_max(my_list):
    # tmp_list = my_list
    tmp_list = my_list.copy()
    tmp_list.sort()
    print(my_list)
    return tmp_list[-2]

def make_positive(my_list):
    for i in range(0, len(my_list)):
        if my_list[i] < 0:
            my_list[i] = abs(my_list[i])

my_list =  input_list()

print('My original list:', my_list)

print('Second largest integer in list is', second_max(my_list))

make_positive(my_list)

print('My now positive list is', my_list)
