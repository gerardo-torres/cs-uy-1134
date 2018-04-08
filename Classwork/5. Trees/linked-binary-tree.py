class LinkedBinaryTree:
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
        
    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def subtree_count(self, curr_root):
        """ draws another recursive tree exactly like the original and a maximum of 2n excess
        nodes for each leaf. """
        if curr_root is None:
            return 0
        else:
            left = self.subtree_count(curr_root.left)
            right = self.subtree_count(curr_root.right)
            return left + right + 1

    def height(self):
        if self.is_empty:
            raise Exception("Structure is empty")
        return self.subtree_height(self, self.root)

    def subtree_height(self, curr_root):
        if curr_root.left == None and curr_root.right == None:
            return 0
        elif curr_root.right is None:
            return 1 + subtree_heigh(curr_root.right)
        elif curr_root.left is None:
            return 1 + subtree_heigh(curr_root.left)
        else:
            left_height = self.subtree_height(curr_root.left)
            right_height = self.subtree_height(curr_root.right)
            return 1 + max(left_height, right_height)

    def preorder(self):
        yield from self.subtree_preorder(self.root)
    
    def subtree_preorder(self, curr_root):
        if curr_root.is None:
            return
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)
    
    def inorder(self):
        yield from self.subtree_inorder(self.root)
    
    def subtree_inorder(self, curr_root):
        if curr_root.is None:
            return
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, curr_root):
        if curr_root.is None:
            return
        else:
            yield from self.subtree_postorder(curr_root.left)
            yield from self.subtree_postorder(curr_root.right)
            yield curr_root

    def breadth_firt(self):
        pass

    def subtree_breadth_firt(self, curr_root):
        pass

    def __iter__(self):
        """preorder: DLR
        inorder: LDR
        postorder: LRD
        breadth-frist: level-by-level"""
        for noed in self.postorder():
            yield node.data

p1 = LinkedBinaryTree.Node(1)
p2 = LinkedBinaryTree.Node(6)
p3 = LinkedBinaryTree.Node(2, p1, p2)
p4 = LinkedBinaryTree.Node(4)
p5 = LinkedBinaryTree.Node(5, p3, p4)

tree = LinkedBinaryTree()