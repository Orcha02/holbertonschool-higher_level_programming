#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = abs(number) % 10 * -1
else:
    last_digit = number % 10

# abs-> To calculate absolute of a number
# end-> allows to append conditionals in same line
# Without the end it will be in diferent lines

print("Last digit of {} is {}".format(number, last_digit), end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
