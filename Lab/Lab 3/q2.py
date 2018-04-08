# Created by: Gerardo Torres
# Net ID: N15561823
# Question 2

def intersection_lst(lst1, lst2):
    """ creates a list from two sorted lists. """
    lst3 = [None] * len(lst1)
    index_1 = 0
    index_2 = 0
    index_3 = 0
    while index_1 < len(lst1):
        if lst1[index_1] == lst2[index_2]:
            lst3[index_3] = lst1[index_1]
            index_1 += 1
            index_2 = 0
            index_3 += 1
        elif lst1[index_1] < lst2[index_2]:
            index_1 += 1
            index_2 = 0
        elif lst1[index_1] > lst2[index_2]:
            index_2 += 1
    # another for loop that deletes
    return lst3

print(intersection_lst([1,6,14,15], [2, 6, 14, 19]))
