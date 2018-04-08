"""Assume that when calling count_down on a smaller range it would
print the numbers of that range in decreasing order. """


# start <= end
def count_down(start, end):
    if start == end:
        return start
    else:
        print(end)
        count_down(start, end - 1)


# start <= end
def count_up_and_down(start, end):
    if start == end:
        return start
    else:
        print(start)
        count_down(start + 1, end)
        print(start)


"""Assume that when calling factorial with k(<n) it would return
k!. """
# n >= 1
def factorial(n):  # T(n) = O(n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


""" Assume that when calling count_appereances on a smaller list 
it would return the number of times val appears in that list. """
# size of the input is the length of the list
def count_apperances(lst, val):  # this implimentation is n^2 because the slicing is linear
    if len(lst) == 0:
        return 0
    else:
        if lst[0] == val:
            return count_apperances(lst[1:], val) + 1
        else:
            return count_apperances(lst[1:], val)


print(count_apperances([1, 3, 2, 4, 2, 43], 2))


""" Assume that when calling count_apperances_2 on a smaller list
it would return the number of times val appears ont aht list. """
# interface
def count_apperances_2(lst, val):
    return count_apperances_2_helper(lst, 0, len(lst), val)

# recursive algorithm
def count_apperances_2_helper(lst, low, high, val):  # linear algorithm
    if low == high:
        if lst[low] == val:
            return 1
        else:
            return 0
    else:
        if lst[low] == val:
            return count_apperances_2_helper(lst, low + 1, high, val) + 1
        else:
            return count_apperances_2_helper(lst, low, high, val)
