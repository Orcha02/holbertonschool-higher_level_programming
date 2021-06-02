#!/usr/bin/python3
""" Class MyList that inherits from list """


class MyList(list):
    def print_sorted(self):
        print(sorted(self))

# sorted-> Prints list in ascending sort
