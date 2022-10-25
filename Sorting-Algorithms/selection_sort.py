from contextlib import nullcontext
from optparse import Values
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def selection_sort(values):
    # a new list that will contain sorted elments
    sorted_list = []

    # to visualilze the sorting and element shifting process among lists
    # before shifting process
    print("%-25s %-25s" % (values, sorted_list))

    # iterating throught elements to find index of shortest and 
    # shifting to the sorted list
    for _ in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))

        # visualize lists after element has been shifted
        print("%-25s %-25s" % (values, sorted_list))

    return sorted_list

def index_of_min(values):

    min_index = 0

    for i in range(1, len(values)):
        
        if values[i] < values[min_index]:
            min_index = i

    return min_index

print(selection_sort(numbers))