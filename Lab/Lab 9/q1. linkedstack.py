class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if(self.is_empty()):
          raise Exception("List is empty")
        return self.header.next

    def last_node(self):
        if(self.is_empty()):
          raise Exception("List is empty")
        return self.trailer.prev

    def add_after(self, node, data):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data, prev, succ)
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_first(self, data):
        return self.add_after(self.header, data)

    def add_last(self, data):
        return self.add_after(self.trailer.prev, data)

    def add_before(self, node, data):
        return self.add_after(node.prev, data)

    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        self.delete_node(self.first_node())

    def delete_last(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        self.delete_node(self.last_node())

    def __iter__(self):
        if (self.is_empty()):
            return
        cursor = self.first_node()
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"

class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.number_of_elements = 0
        
    def push(self, e):
        ''' Add element e to the top of the stack '''
        self.data.add_last(e)
        self.number_of_elements += 1
    
    def pop(self):
        ''' Remove and return the top element from the stack. If the
        stack is empty, raise an exception'''
        if self.data.is_empty():
            raise Exception("LinkedStack is empty")
        last_node = self.data.last_node()
        self.number_of_elements -= 1
        self.data.delete_last()
        return last_node.data
    
    def top(self):
        ''' Return a reference to the top element of the stack without
        removing it. If the stack is empty, raise an exception '''
        if self.data.is_empty():
            raise Exception("LinkedStack is empty bruh")
        top_node = self.data.last_node()
        return top_node.data()
    
    def is_empty(self):
        ''' Return True if stack is empty'''
        return self.data.is_empty()
    
    def __len__(self):
        '''Return the number of elements in the stack'''
        return self.number_of_elements()
    
    def __repr__(self):
        return self.data.__repr__()

def main():
    L = LinkedStack()
    L.push(3)
    L.push(4)
    print(L)
    L.pop()
    print(L)

main()