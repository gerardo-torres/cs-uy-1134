def remove_all_evens(lst):
    i = 0
    length = len(lst)
    even_count = 0
    while i < length:
        if lst[i] % 2 == 0:
            lst.append(lst[i])
            even_count += 1
        i += 1
    for i in range(even_count):
        lst.pop()
    for i in range(len(lst)):
        
        


def main():
    lst = [2, 3, 5, 2, 16, 13, 2, 2, 2]
    remove_all_evens(lst)
    print(lst)

def main2():
    lst2 = [2, 3, 5, 2, 16, 13]
    remove_all_evens(lst2)
    print(lst2)

main()
main2()