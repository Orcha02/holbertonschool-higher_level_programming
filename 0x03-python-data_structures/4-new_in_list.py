#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_my_list = my_list[:]  # To not modify original list
    if idx < 0:
        return cp_my_list
    elif idx >= len(my_list):
        return cp_my_list
    else:
        cp_my_list[idx] = element
        return cp_my_list
