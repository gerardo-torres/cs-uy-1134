lst = [[1, 2], [3, [[4],5]], 6]

def total_nest_helper(lst, abs_start, abs_end, start, end, total):
    if abs_start == abs_end:
        return total + lst[end]
    else:
        if isinstance(lst[abs_start], list):
            return total + total_nest_helper(lst, abs_start, abs_end, start + 1, end, total) + total_nest_helper(lst[start], abs_start, abs_end, 0, len(lst[start]) - 1, total)
        else:
            return total + total_nest_helper(lst, abs_start + 1, abs_end, start + 1, end, total + lst[start])

print(total_nest_helper(lst, 0, len(lst) - 1, 0, len(lst) - 1, 0))

def sum_list(lst):
    return (sum_list_helper(lst,0,len(lst)-1))
def sum_list_helper(lst,low,high):
    if low == high and isinstance(lst[low],list)!=True):
        return lst[low]
    elif (low==high and isinstance(lst[low],list)==True):
        return sum_list(lst[low])

    else:
        rest=sum_list_helper(lst,low+1,high)
        if isinstance(lst[low],list):
            return rest+sum_list(lst[low])
        else:
            return rest+lst[low]