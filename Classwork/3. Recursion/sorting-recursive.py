# Created by: Gerardo Torres
# cs-uy 1134
# 2-26-2018

def merge_sort(lst):
    merge_sort(lst, 0, len(lst) - 1)

def merge_sort_helper(lst, low, high):
    if low == high:
        return
    else:
        mid = (low + high) // 2
        merge_sort_helper(lst, lo w, mid)
        merge_sort_helper(lst, mid + 1, high)
        merge(lst, low, mid, high)
