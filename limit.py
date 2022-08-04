# This program calculates the limit of a function.

import math

print("You may use math functions such as 'math.sqrt(x)' when typing your function. You may also use inf or -inf for ∞ or -∞ respectively for your limit.")

limit = float(input("Enter the limit:"))
function = input("Enter your function:")

print(function)

try:
    x = limit
    print(f"The function goes to {eval((function))}")
except:
    x = limit - 0.00000001
    print(f"The function goes to {eval((function))}")
