#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) is 1:
        print("{:d} argument:".format(len(sys.argv) - 1))
    elif len(sys.argv) is 0:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{:d}: {}".format(i, sys.argv[i]))
# -1 so it doesnt count the "arguments:" to the sum of the real arguments
