#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Peak in a list of unsorted integers """
    if len(list_of_integers) == 0:
        return None
    return max(list_of_integers)
