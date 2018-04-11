lst = [[1, 2], [3,[[4], 5]], 6]

def sum_flat(lst):
    sum_ = 0
    for elem in lst:
        if isinstance(elem, lst):
            sum_ += sum_flat(elem)
        else:
            sum += elem
        return sum_