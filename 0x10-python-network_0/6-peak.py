#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Peak in a list of unsorted integers """
    if type(list_of_integers) == list:
        if len(list_of_integers) == 0:
            return None
        list_of_integers.sort()
        return list_of_integers[-1]
    return None

# [-1]-> Returns the last value in the resulting list
