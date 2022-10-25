import numbers
import random
# The sys.argv list gives su the command line arguments to the
# script. To use it, we also nedd to import the "sys" module.
import sys
# Importing the load_numbers function 
from load import load_numbers

# Here, we pass the first command line argument (which should be the path to a file)
# to load_numbers, and store the returned list of nubmers in a variable.
numbers = load_numbers(sys.argv[1])

# Bogosort just randomly rearranges thelist of balues over and over,
# so the first thing it's going to need is a function to detect when
# the list is sorted. We'll write an is_sorted function that takes a 
# list of values as a parameter. It will return True if the list passed 
# in is sorted, or False if it isn't.

def is_sorted(values):
    for index in range(len(values) - 1):
        # if the list is sorted, then every value in it will be less 
        # than the one that comes after it. So we test to see whether the 
        # current item is GREATER than the one that follows it.
        if values[index] > values[index + 1]:
            # If it is then the whole list is not sorted
            return False
    # Loop completed without finding any unsorted values
    return True

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values

print(bogo_sort(numbers))