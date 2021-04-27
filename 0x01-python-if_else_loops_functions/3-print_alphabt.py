#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    # +1-> Para q salga la 'z'
    if i == ord('q') or i == ord('e'):
        continue
    print("{:c}".format(i), end="")
