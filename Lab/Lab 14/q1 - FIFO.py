"""
Implement the FIFO queue ADT with the following methods using only a priority
queue and one additional integer as data members.
- q.enqueue(elem)
- q.dequeue()
- q.first()
- len(q)
- q.is_empty()
"""
class ArrayMinHeap:

    class Item:
        def __init__(self, priority, value=None):
            self.priority = priority
            self.value = value

        def __lt__(self, other):
            return self.priority < other.priority

        def __repr__(self):
            return str(self.value)
        
    def __init__(self):
        self.data = [None]

    def __len__(self):
        return len(self.data) - 1

    def left(self, i):
        return 2 * i

    def right(self, i):
        return (2 * i) + 1

    def parent(self, i):
        return i // 2

    def has_left(self, i):
        try:
            self.data[self.left(i)]
            return True
        except IndexError:
            return False

    def has_right(self, i):
        try:
            self.data[self.right(i)]
            return True
        except IndexError:
            return False

    def is_empty(self):
        return len(self) == 0

    def min(self):
        if self.is_empty():
            raise Exception("Heap is empty")
        item = self.data[1]
        return item.priority, item.value

    def insert(self, priority, val=None):
        new_item = ArrayMinHeap.Item(priority, val)
        self.data.append(new_item)
        self.fix_up(len(self.data) - 1)

    def delete_min(self):
        if self.is_empty():
            raise Exception("Heap is empty")
        self.swap(1, len(self.data) - 1)
        item = self.data.pop()
        self.fix_down(1)
        return item.priority, item.value

    def swap(self, i1, i2):
        self.data[i1], self.data[i2] = self.data[i2], self.data[i1]

    def fix_up(self, i):
        if i == 1:
            return
        parent = self.parent(i)
        if self.data[i] < self.data[parent]:
            self.swap(i, parent)
            self.fix_up(parent)

    def fix_down(self, i):
        if self.has_left(i):
            left = self.left(i)
            smaller_child = left
        if self.has_right(i):
            right = self.right(i)
            if self.data[left] < self.data[right]:
                smaller_child = right
        if self.data[smaller_child] < self.data[i]:
            self.swap(smaller_child, i)
            self.fix_down(smaller_child)

    def __iter__(self):
        for i in self.data:
            yield i

class Queue:
    def __init__(self):
        self.data = ArrayMinHeap()
        self.my_priority = 0

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0
    
    def enqueue(self, e):
        self.data.insert(self.my_priority + 1, e)
        self.my_priority += 1

    def dequeue(self):
        return self.data.delete_min()[1]
        
    def first(self):
        return self.data.data[1]

    def __repr__(self):
        string =''
        for i in self.data.data:
            if str(i) == "None":
                pass
            else:
                string += str(i) + ", "
        
        return string

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    queue.dequeue()

main()