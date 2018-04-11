def f(n):
    if n==1:
        return 1
    else:
        print("foo")
        return f(n - 1) + f(n - 1)

def f_c(n):
    if n == 1:
        print(1)
    else:
        f_c(n//2)
        for i in range(n):
            print(i, end = ' ')
        print(' ')

f_c(4)