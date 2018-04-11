
class Empty(Exception):
    pass
    
class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0
        self.back_ind = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return self.num_of_elems == 0

    def add_last(self, elem):
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
        self.back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def add_first(self, elem):
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
        if self.num_of_elems == 0:
            self.add_last(elem)
        elif self.num_of_elems > 0:
            self.num_of_elems += 1
            new_front = (self.front_ind - 1) % len(self)
            self.data[new_front] = elem

    def delete_first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def delete_last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        value = self.data[(self.front_ind + self.num_of_elems) % self.num_of_elems]
        self.data[(self.front_ind + self.num_of_elems - 1) % self.num_of_elems] = None
        self.num_of_elems -= 1
        if(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]
    
    def last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[(self.front_ind + self.num_of_elems) % self.num_of_elems]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

    def __repr__(self):

        return str([self.data[i] for i in range(self.front_ind, self.front_ind + self.num_of_elems + 1) if self.data[i] != None])

q = ArrayQueue()
q.add_first('4')
q.add_last('5')
q.add_first('3')
print(q.last())
q.delete_first()
q.delete_last()
print(q)