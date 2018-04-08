class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.parent = None
        self.left = left
        if left is not None:
            self.left.parent = self
        self.right = right
        if right is not None:
            self.right.parent = self

p1 = Node(1)
p2 = Node(6)
p3 = Node(2, p1, p2)
p4 = Node(4)
p5 = Node(5, p3, p4)
