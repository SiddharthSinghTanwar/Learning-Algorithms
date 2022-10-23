def mergeSort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    Divide: find the midpoint of list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: merge the sorted sublists created in previous step
    Takes O(n log n) time
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = mergeSort(left_half)
    right = mergeSort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    Takes overall O(log n) time
    Caveat: slicing operation takes O(k) time, k represents the sliced slice
    thus overall it takes O(k nlog n)
    """

    mid = len(list)//2

    left = []
    right = []
    i = 0
    j = mid
    while i < mid:
        left.append(list[i])
        i += 1
    while j < len(list):
        right.append(list[j])
        j += 1
        
    return left, right

def merge(left, right):
    """
    Merges two lists sorting them in the process
    Returns a new merged list
    Takes O(n) time
    """

    l = []
    i = 0
    j = 0

    while(i < len(left) and j < len(right)):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1
    
    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

alist = [54,34,55,67,77,3,52,43]
l = mergeSort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))