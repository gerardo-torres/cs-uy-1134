def f():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x

collection = f()  # making a generator

print(type(collection)) 

coll_iter = iter(collection) # making an iterable collection

print(next(coll_iter))
print(next(coll_iter))
print(next(coll_iter))

"""

for i in f():  # not f, but a call to f().
    print(i)

"""

def my_range_lst(start, end, step):
    """ low level implmentation of a range - with yield this time. """
    curr = start
    while curr < end:
        yield curr
        curr +=  step


for elem in my_range_lst(3, 10, 0.5):
    print(elem)
