def remove_all_evens(lst):
    i = 0
    last_ind = len(lst) - 1
    while i <= len(lst) and i <= last_ind:
        if lst[i] % 2 == 0:
            lst[i], lst[last_ind] = lst[last_ind], lst[i]
            last_ind -= 1
        if lst[last_ind] % 2 == 0:
            last_ind -= 1
        i += 1
    for i in range((len(lst) - 1) - last_ind):
        lst.pop()

lst = [2, 3, 5, 2, 16, 13, 6, 6, 6, 6]

remove_all_evens(lst)
print(lst)
