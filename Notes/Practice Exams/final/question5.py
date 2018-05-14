class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (left is not None):
                self.left.parent = self
            self.right = right
            if (right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def subtree_count(self, curr_root):
        if(curr_root is None):
            return 0
        else:
            left_count = self.subtree_count(curr_root.left)
            right_count = self.subtree_count(curr_root.right)
            return left_count + right_count + 1

    def height(self):
        if(self.is_empty()):
            raise Exception("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    def subtree_height(self, curr_root):
        if((curr_root.left is None) and (curr_root.right is None)):
            return 0
        elif(curr_root.right is None):
            return 1 + self.subtree_height(curr_root.left)
        elif(curr_root.left is None):
            return 1 + self.subtree_height(curr_root.right)
        else:
            left_height = self.subtree_height(curr_root.left)
            right_height = self.subtree_height(curr_root.right)
            return 1 + max(left_height, right_height)

    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, curr_root):
        if(curr_root is None):
            return
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)

    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, curr_root):
        if (curr_root is None):
            return
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, curr_root):
        if (curr_root is None):
            return
        else:
            yield from self.subtree_postorder(curr_root.left)
            yield from self.subtree_postorder(curr_root.right)
            yield curr_root

    def __iter__(self):
        for node in self.postorder():
            yield node.data


def main():
    node1 = LinkedBinaryTree.Node(1)
    node3 = LinkedBinaryTree.Node(3)
    node2 = LinkedBinaryTree.Node(2, node1, node3)
    node6 = LinkedBinaryTree.Node(6)
    node9 = LinkedBinaryTree.Node(9)
    node7 = LinkedBinaryTree.Node(7, node6, node9)
    root = LinkedBinaryTree.Node(4, node2, node7)
    lbt = LinkedBinaryTree(root)
    for i in lbt:
        print(i)
    return lbt

def level_list(root, level):
    if root is None:
        return []
    if level == 0:
        return [root.data]
    else:
        left = level_list(root.left, level - 1)
        right = level_list(root.right, level - 1)
        lst = left + right
    return lst

def level_list2(root, level):
    if root is None:
        return []
    else:
        left = level_list2(root.left, level - 1)
        right = level_list2(root.right, level - 1)
        if level == 0:
            return [root.data]
    return left + right


lbt = main()
print(level_list(lbt.root, 2))
