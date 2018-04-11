# Created by: Gerardo Torres
# Lab 5 Question 2

lst = [1, 2, 3, 4, 5, 100, 12, 2]

def product_evens(lst, low):
    if low == len(lst) - 1:
        if lst[low] % 2 == 0 and lst[low] < len(lst):
            return lst[low]
        else:
            return 1
    else:
        rest = product_evens(lst, low + 1)
        if lst[low] % 2 == 0 and lst[low] < len(lst):
            return rest * lst[low]
        else:
            return rest * 1

print(product_evens(lst, 0))
