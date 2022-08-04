# This code outputs a number of Fibonacci numbers and also determines whether they are prime.

import math
fib = [0, 1]
prime_numbers = []
reply = ""

def prime(number):
    if number < 2:
        return False
    for x in range (2, math.ceil(math.sqrt(number+1))):
        if number % x == 0:
            return False
    return True

user_input = int(input("How many values of the Fibonacci sequence would you like to calculate?\t"))

while reply not in ["y", "yes", "n", "no"]:
    reply = input("Would you like to determine whether the number is prime? This adds significant time for n values higher than ~100. (y/n)\t").lower()
    if reply not in ["y", "yes", "n", "no"]:
        print("Please enter a valid choice...")

for x in range(0, user_input):
    fib.append(fib[-2] + fib[-1])

if reply.lower in ["y", "yes"]:
    for value in fib:
        print(f"{fib.index(value)}: {value}")
        if prime(value):
            print(f"\n{value} is prime!\n")
            prime_numbers.append(value)
else:
    print(fib)
    print(f"The last number is {len(str(fib[-1]))} digits long")