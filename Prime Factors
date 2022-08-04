# This will display a list of the prime factors of a number if any exist.
# Prime numbers are determined from range(0 to square root of number for substantially faster calculations for large numbers)

import math

def prime(number):
    if number < 2:
        return False
    for x in range (2, math.ceil(math.sqrt(number + 1))):
        if number % x == 0:
            return False
    return True

def factor(number):
    for x in range (1, number + 1):
        if number % x == 0:
            factors.append(x)
    return factors

def prime_factor(factors):
    for factor in factors:
        if prime(factor):
            prime_factors.append(factor)
    return prime_factors
    
while True:
    factors = []
    prime_factors = []

    value = int(input("Enter a number and I will find the prime factors if any exist:\t"))
    
    factor(value)
    prime_factor(factors)
    
    print(f"All factors: {factors}")

    if prime_factors != []:
        print(f"Prime factors: {prime_factors}")
    else:
        print(f"There are no prime factors for {value}")
