# Flips a coin and outputs how many times it was heads/tails.

import random

def flip(times):
    choices = ["Heads", "Tails"]
    heads, tails = 0, 0
    
    for x in range(0, times):
        flip = random.choice(choices)
        if flip == "Heads":
            heads+=1
        elif flip == "Tails":
            tails+=1
        
    print(f"\nHeads:\t{heads}\nTails:\t{tails}")

while True:
    try:
        flip(int(input("How many times would you like to flip a coin?\t")))
    except:
        print("Please type a valid number...\n")
