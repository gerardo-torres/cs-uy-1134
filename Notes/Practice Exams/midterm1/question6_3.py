def remove_all_evens(lst):
    low = 0
    high = len(lst) - 1
    even = 0
    while low <= high:
        if lst[low] % 2 == 0 and lst[high] % 2!= 0:
            lst[high], lst[low] = lst[low], lst[high]
            low += 1
            high -= 1
            even += 1
        elif lst[low] % 2 == 0 and lst[high] % 2 == 0:
            even += 1
            high-=1
        elif lst[low] % 2 != 0 and lst[high] % 2 == 0:
            low += 1
            high -= 1
            even += 1
        elif lst[low] % 2 != 0 and lst[high] % 2 != 0:
            low += 1
    for i in range(even):
        lst.pop()

def main():
    lst = [3, 7, 2, 4, 10, 9, 6, 8]
    remove_all_evens(lst)
    print(lst)


main()
