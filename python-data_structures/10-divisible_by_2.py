#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if not my_list:
        return
    new_list = []
    for x in range(len(my_list)):
        if x % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
