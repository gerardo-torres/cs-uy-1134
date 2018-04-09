class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self) == 0)

    def push(self, elem):
        self.data.append(elem)

    def pop(self):
        if (self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.data.pop()

    def top(self):
        if (self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.data[-1]
    
    def __repr__(self):
        return str([self.data[i] for i in range(len(self.data))])

class EmptyCollection(Exception):
    pass

class DupStack:
    def __init__(self):
        self.data = ArrayStack()
        self.num_of_elems = 0

    def __len__(self):
        return self.num_of_elems
    
    def is_empty(self):
        return (self.num_of_elems == 0)

    def push(self, e):
        if (not self.is_empty()) and (self.data.top()[0] == e):
            old = self.data.pop()
            new = (old[0], old[1] + 1)
            self.data.push(new)
        else:
            tup = (e, 1)
            self.data.push(tup)
        self.num_of_elems += 1

    def top(self):
        if (self.is_empty()):
            raise EmptyCollection("Duplicates Stack is empty")
        return self.data.top()[0]
    
    def top_dups_count(self):
        if (self.is_empty()):
            raise EmptyCollection("Duplicates Stack is empty")
        return self.data.top()[1]
    
    def pop(self):
        if (self.is_empty()):
            raise EmptyCollection("Duplicates Stack is empty")
        popped = self.data.top()[0]
        old = self.data.pop()
        new = (old[0], old[1] - 1)
        self.data.push(new)
        if self.data.top()[1] == 0:
            self.data.pop()
        self.num_of_elems -= 1
        return popped

    def pop_dups(self):
        if (self.is_empty()):
            raise EmptyCollection("Duplicates Stack is empty")
        popped = self.data.top()[0]
        self.num_of_elems -= self.data.top()[1]
        self.data.pop()
        return popped
    
    def __repr__(self):
        return self.data.__repr__()

def main():
    dupS = DupStack()
    dupS.push(4)
    dupS.push(5)
    dupS.push(5)
    dupS.push(5)
    dupS.push(4)
    dupS.push(4)
    print(dupS)
    print(len(dupS))
    print(dupS.top())
    print(dupS.top_dups_count())
    print(dupS.pop())
    print(dupS.pop())
    print(dupS.top())
    print(dupS.top_dups_count())
    print(dupS.pop_dups())
    print(dupS.top())
    print(dupS)

main()