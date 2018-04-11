import ctypes  # Provides low-level arrays

def make_array(n):
    return (n * ctypes.py_object)()


class Mylist:
    def __init__(self):
        self.data = make_array(1)
        self.n = 0
        self.capacity = 1
    
    def __len__():
        return self.n
    
    def append(self, val):
        if self.n == self.capacity:  # resizing if the array is full
            self.resize(2 * self.n)  # calling the resize method
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):  # copying the data from the old array
            new_array[i] = self.data[i]
        self.data = new_array  # setting the data to be equal to the new array
        self.capacity = new_size  # doubling the capacity of the array

    def __getitem__(self, ind):
        if not (0 <= ind <= (self.n -1)):  # restricting the use of negative indecies and indecies outside of the self.n
            raise IndexError("Invalid Index")
        return self.data[ind]

    def __setitem__(self, ind, val):
        if not (0 <= ind <= (self.n -1)):  # restricting the use of negative indecies and indecies outside of the self.n
            raise IndexError("Invalid Index")
        self.data[ind] = val

    def __repr__(self):
        pass
    
    def __iter__(self):
        for i in range(self.m):
            yield self.data[i]


lst = Mylist()
for i in range(5):
    lst.append(i+1)
print(lst[3])