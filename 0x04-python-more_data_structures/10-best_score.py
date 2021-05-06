#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        biggest_value_key = max(a_dictionary)
        return biggest_value_key
