def sort_first(lst):
    first = lst[0]
    lst.append(lst.pop(0))
    for i in range(len(lst)):
        if lst[i] < first:
            pass
        elif lst[i] > first:
            lst.append(lst.pop(i))

def sort_first_recur(lst, low, high, first):
    print(lst)
    if low > high:
        return
    else:
        if lst[high] < first:
            lst.insert(0, lst.pop(high))
            sort_first_recur(lst, low, high - 1, first)
        else:
            sort_first_recur(lst, low, high - 1, first)

lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sort_first_recur(lst, 0, len(lst) - 1, 54)
print(lst)
