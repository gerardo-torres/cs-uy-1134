import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.n = 0
        self.capacity = 1

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2*self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data[i]
        self.data = new_arr
        self.capacity = new_size

    def __len__(self):
        return self.n

    def __getitem__(self, ind):
        if (not(0 <= ind <= (self.n - 1))):
            raise IndexError("invalid index")
        return self.data[ind]

    def __setitem__(self, ind, val):
        if (not(0 <= ind <= (self.n - 1))):
            raise IndexError("invalid index")
        self.data[ind] = val

    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]

    def extend(self, iterable_collection):
        for elem in iterable_collection:
            self.append(elem)