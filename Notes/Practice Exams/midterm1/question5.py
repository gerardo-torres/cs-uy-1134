""" Below, you are given a recursive implementation for the function:
    def min_in_lst(lst, low, high)
    
    this function gets the list of integers lst, as well as two indices: low and high
    (low <= high), which indicate the range of indicies of the elements that should to
    be considered.
    When called, the function would return the minimum value out of all the elements
    in the low, low + 1 ..., high postitions."""

def min_in_lst(lst, low, high):
    if low == high:
        return lst[low]
    else:
        mid_in = (low + high) // 2
        min1 = min_in_lst(lst, low, mid_in)
        min2 = min_in_lst(lst, mid_in, high)
        if min1 < min2:
            return min1
        else:
            return min2

lst = [1, 3, 4]

print(min_in_lst(lst, 0, len(lst) - 1))
