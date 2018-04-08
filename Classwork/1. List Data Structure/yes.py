def main():
    lst = [1, 2, 3]
    s = "abc"
    func(lst, s)
    print("main lst =", lst, "s =", s)


def func(lst, s):
    for ind in range(len(lst)):
        lst[ind] += 10
    lst.append(6)
    s.upper()  # Didn't store this data
    print("func: lst=", lst, "s =", s)


main()
