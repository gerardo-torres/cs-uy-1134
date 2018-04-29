def my_hash(i):
    a = 1
    b = 2
    p = 107
    n = 7
    return ((((a * i) + b) % p) % n)

"""
a. Insert 37
b. Insert 47
c. Insert 51
d. Delete 37
e. Insert 65
f. Insert 104
g. Insert 8
h. Insert 5
i. Insert 10
j. Insert 7
k. Delete 8
"""


"""
print('37', my_hash(37))
print('47', my_hash(47))
print('51', my_hash(51))
print('37', my_hash(37))
print('65', my_hash(65))
print('104', my_hash(104))
print('8', my_hash(8))
print('5', my_hash(5))
print('10', my_hash(10))
print('7', my_hash(7))"""


def division(i, n):
    return (i % n)

def main():
    print(division(37, 7))
    print(division(47, 7))
    print(division(51, 7))
    print(division(37, 7))
    print(division(37, 7))
    print(division(47, 7))

main()