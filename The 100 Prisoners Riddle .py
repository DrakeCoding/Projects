# This code was created after watching "The Riddle That Seems Impossible Even If You Know The Answer" by Veritasium on Youtube: https://www.youtube.com/watch?v=iSNsgj1OCLA
# There are 100 prisoners with numbers 1-100. 100 boxes are placed in a room with a number 1-100 in each of the boxes. The prisoners go in one by one and search 50 boxes.
# If all 100 are able to find their box within 50 tries, they all escape prison. If any of them fail to find their number, they all die.
# As iterations increase, the outcome to this problem approaches 1 - ln2 ≈ 0.30685 or 30.685%

from random import shuffle
from tqdm import tqdm

prisoners = [num for num in range(1,101)] # Creates a list [1, 2, 3, 4, ..., 99, 100]
boxes = prisoners[:] # Creates a copy of the list above
shuffle(boxes) # Shuffles the numbers in the 'boxes' the prisoners are looking in

def check_boxes(prisoner_number):
    number_in_box = prisoner_number

    for _ in range(50):
        number_in_box = boxes[number_in_box - 1] # The prisoner looks inside the box and gets the number inside that box
        if number_in_box == prisoner_number: # If the number in the box is the prisoner's number they have completed the challenge
            return True
    return False # If none of the numbers inside the boxes match the prisoner's number, the prisoner fails.

def escape():
    for prisoner in prisoners: # For each prisoner with number in [1, 2, 3, 4, ..., 99, 100] do the following:
        if check_boxes(prisoner) is False: # If any of the prisoner's fail, they all do so return False
            return False
    return True # If none of the prisoners fail the challenge, they win so return true

escaped, died = 0, 0 # Sets values to 0 so we can count the amount of times escaped and amount of times died later.
iterations = 100000 # This is how many times the computer will run the test. Change it to change the amount of tests.

for _ in tqdm(range(iterations), 'Iterations'): # Runs the test 'iterations' amount of times. tqdm shows a progress bar which is useful for running long tests (iterations > 1,000,000)
    shuffle(boxes)    # Shuffles the numbers inside the boxes for each iteration
    if escape():
        escaped += 1 # Counts the amount of times escaped.
    else:
        died += 1 # Counts the amount of times lost.

print(f"\nEscaped\t: {escaped:,}.\nDied\t: {died:,}.\nYou escaped {escaped/iterations:.2%} of the time\n")