#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dgt = abs(number) % 10
print(f"Last digit of {number} is {dgt}", end=" ")
if dgt > 5:
    print("and is greater than 5")
elif dgt == 0:
    print("and is 0")
else:
    print(f"and is less than 6 and not 0")
