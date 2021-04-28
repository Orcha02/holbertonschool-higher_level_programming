#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) is 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
        # To show not just "argument" and the count, but the actual argument
        print("{:d}: {}".format(len(sys.argv) - 1, sys.argv[1]))
    elif len(sys.argv) is 1:
        print("{:d} arguments.".format(len(sys.argv) - 1))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{:d}: {}".format(i, sys.argv[i]))
# -1 so it doesnt count the "arguments:" to the sum of the real arguments
# 2 instead of 1 and 1 instead of 0 to correct output due to -1
