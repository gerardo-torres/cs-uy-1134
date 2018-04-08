from DoublyLinkedList import *

class BoostQueue:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.number_of_elems = 0

    def __len__(self):
        return self.number_of_elems

    def is_empty(self):
        return self.number_of_elems == 0

    def enqueue(self, elem):
        self.data.add_last(elem)
        self.number_of_elems += 1

    def first(self):
        return DoublyLinkedList.first_node().data
    
    def boost(self, k):
        right = self.data.last_node()
        if(self.is_empty()):
            raise Exception("List is empty")
        if k >= self.number_of_elems:
            k = self.number_of_elems - 1
        for i in range(k):
            left = right.prev
            left.data, right.data = right.data, left.data
            right = right.prev

    def __repr__(self):
        return self.data.__repr__()

    def dequeue(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        return self.data.delete_first()

boost_q = BoostQueue()
boost_q.enqueue(1)
boost_q.enqueue(2)
boost_q.enqueue(3)
boost_q.enqueue(4)
print(boost_q)
boost_q.boost(8)
print(boost_q)
#boost_q.dequeue()
#print(boost_q)
