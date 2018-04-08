### 1 ###
lst = [1, 2, 3]
for elem in lst:
    elem += 10
    print(elem)

lst = [1, 2, 3]
for ind in range(len(lst)):
    lst[ind] += 10



### 2 ###
lst1 = [1, 2, 3]
lst2 = lst1
lst3 = [1, 2, 3]
lst1.append(4)
lst2.append(5)
lst3.append(6)
print("lst1 =", lst1)
print("lst2 =", lst2)
print("lst3 =", lst3)
[


### 3 ###

lst = [[1, 2], 3, [4, 5]]
copy_lst = lst.copy()
copy_lst[0][0] = 10


import copy

lst = [[1, 2], 3, [4, 5]]
shallow_lst = copy.copy(lst) # or lst.copy()
deep_lst = copy.deepcopy(lst)


shallow_lst[0][0] = 10
# lst
# [[10, 2], 3, [4, 5]]
# shallow_lst
# [[10, 2], 3, [4, 5]]
# deep_lst
# [[1, 2], 3, [4, 5]]

deep_lst[0][1] = 20
# lst
# [[10, 2], 3, [4, 5]]
# shallow_lst
# [[10, 2], 30, [4, 5]]
# deep_lst
# [[1, 20], 3, [4, 5]]

shallow_lst[1] = 30
# lst
# [[10, 2], 3, [4, 5]]
# shallow_lst
# [[10, 2], 30, [4, 5]]
# deep_lst
# [[1, 2], 3, [4, 5]]



### 4 ###
def main():
    main_lst1 = [1, 2, 3]
    fun1(main_lst1)
    print("main_lst1 =", main_lst1)

    main_lst2 = [1, 2, 3]
    fun2(main_lst2)
    print("main_lst2 =", main_lst2)


def fun1(lst):
    for ind in range(len(lst)):
        lst[ind] += 10
    print("lst =", lst)


def fun2(lst):
    lst.append(4)
    lst = [1, 2, 3]
    lst.reverse()
    print("lst =", lst)