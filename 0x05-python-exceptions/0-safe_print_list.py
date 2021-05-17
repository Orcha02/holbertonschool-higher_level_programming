#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for elements in my_list:
            print("{}".format(elements), end="")
            counter += 1
    except IndexError:
        print("Invalid Index")
    finally:
        print()
        return counter

# finally-> Will print if there's an error or not
