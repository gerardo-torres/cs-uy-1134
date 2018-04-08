import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()


class MyList():
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n

    def __repr__(self):
        str_list = MyList()
        for i in self:
            str_list.append(str(i))
        return "[" + ", ".join(str_list) + "]"

    def append(self, val):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size

    def extend(self, other):
        for elem in other:
            self.append(elem)

    def __getitem__(self, index):
        if index < 0:  # converting to positive notation
            index += self.n
        if not(0 <= index <= (self.n - 1)):  # checking if the index is within range
            raise IndexError("Index out of range")
        return self.data[index]

    def __mul__(self, n):
        new_list = MyList()
        for i in range(n):
            new_list.extend(self.data)
        return new_list

    def __setitem__(self, index, val):
        if index < 0:  # converting to positive notation
            index += self.n
        if not(0 <= index <= (self.n - 1)):  # checking if the index is within range
            raise IndexError("Index out of range")
        self.data[index] = val

    def __iter__(self):
        for i in range(len(self)):
            yield self.data[i]
            # alternatively, could say yield self[i], which will call __getitme__()
    
    def __add__(self, mylist2):
        new_list = MyList()
        for j in self:
            new_list.append(j)
        for i in range(len(mylist2)):
            new_list.append(mylist2.data[i])
        return new_list
    
    def __iadd__(self, mylist2):
        new_list = MyList
        for j in range(len(self)):
            new_list.append(self.data[j])
        new_list.data = self.data
        for i in range(len(mylist2)):
            new_list.append(mylist2.data[i])
        return new_list
    
    def insert(self, index, val):
        if index < 0:  # converting to positive notation
            index += self.n
        if not(0 <= index <= (self.n - 1)):
            raise IndexError("Index out of range")
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        for i in range(self.n, index - 1, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = val
        self.n += 1
    
    def pop(self):
        if self.n == 0:
            raise IndexError("Index out of range")
        if self.n <= 0.25 * self.capacity:
            self.capacity *= 0.5
        last = self.data[self.n - 1]
        self.data[self.n - 1] = None
        self.n -= 1
        return last
      

def main():
    lst = MyList()
    lst.append(3)
    lst.append(4)
    lst2 = MyList()
    lst2.append(5)
    lst2.append(6)
    lst3 = lst + lst2
    # print(lst3)
    # print(lst * 3)
    mlst = MyList()
    # for i in range(1, 5):
    #     mlst.append(i)
    # mlst.insert(2, 30)
    # print(mlst)
    for i in range(1, 6):
        mlst.append(i)
    print(mlst.pop())
    print(mlst.pop())
    print(mlst.pop())
    print(mlst.pop())
    print(mlst)

