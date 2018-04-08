def is_sorted(lst, low, high):
    if low >= high:
        return True
    else:
        is_sor = is_sorted(lst, low + 1, high)
        if lst[low] > lst[low + 1]:
            is_sor = False
        return is_sor

def main():
    lst = [1, 7, 2]
    print(is_sorted(lst, 0, len(lst) - 1))

main()
