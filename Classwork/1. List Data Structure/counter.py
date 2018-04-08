class Counter:
    def __init__(self):
        self.value = 0
    
    def inc(self):
        self.value += 1

    def __repr__(self):
        return str(self.value)


a = [Counter] * 3  # creates one counter object and changes the values of each item
for c in a:
    c().inc()
    print(c())  # prints "123"

b = [Counter for i in range(3)]  # creates three different new counter objects
for c in b:
    c().inc
    print(c)  # prints "111"


def shallow_copy(lst):
    """ returns a shallow copy of the list. """
    return [item for item in lst]


s ="abc"
for element in s:
    print(s)

str_iter = iter(s)
go = True
while go:
    """ Low level implimentation of a for loop. """
    try:
        elem = next(str_iter)
        print(elem)
    except StopIteration:
        go = False

for elem in range(3, 10, 0.5):
    print(elem)

def my_range_lst(start, end, step):
    """ low level implmentation of a range. """
    my_lst = []
    curr = start
    while curr < end:
        my_lst.append(curr)
        curr +=  step
    return my_lst
