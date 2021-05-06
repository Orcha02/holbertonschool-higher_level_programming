#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        biggest_value_key = max(a_dictionary, key=a_dictionary.get)
        return biggest_value_key

# max-> Returns the item with the highest value
# get-> Returns value of the item with the specified key (biggest_value_key)
