#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    elif idx >= len(my_list):
        return (None)
    else:
        return (my_list[idx])
# [idx]-> To correct output "Element at index 3 is [1, 2, 3, 4, 5]"
