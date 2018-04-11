# Created by: Gerardo Torres
# Lab 5 Question 1

lst =[1, 2, 3, 4, 5, 100, 12, 2]

def find_lst_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        highest = find_lst_max(lst[1:])
        if lst[0] > highest:
            highest = lst[0]
        return highest

print(find_lst_max(lst))