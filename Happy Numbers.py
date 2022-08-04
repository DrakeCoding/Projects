import math

happy_numbers = []
prime_happy_numbers = []

def happy_number(value):
    values = []
    sum = value

    while True:
        
        list = []
        sum = str(sum)
        for x in range(0, len(sum)):
            list.append(str(sum[x]))
        
        sum = 0        
        for x in list:
            sum = int(x)**2 + int(sum)
        if sum == 1:
            return True
        if sum in values:
            return False
        values.append(sum)
     
def prime(value):
    if value < 2:
        return False
    for x in range(2, math.ceil(math.sqrt(value + 1))):
        if value % x == 0:
            return False
    return True

user_input = int(input("Enter a number to calculate Happy Numbers for in range(1, number):\t"))

for value in range(1, user_input):
    if happy_number(value):
        happy_numbers.append(value)

for x in happy_numbers:
    if prime(x):
        prime_happy_numbers.append(x)

print(happy_numbers)
print(prime_happy_numbers)
print(f"There are {len(happy_numbers)} Happy Numbers between 1 and {user_input}. {len(prime_happy_numbers)} of them are prime!")
