import LinkedBinaryTree

def rep(bin_tree):
    for node in bin_tree.breadth_first():
        print(node.data)

def invert_binary_tree(binary_tree):
    """ crates a new tree in place """
    if binary_tree.left is None and binary_tree.right is None:
        return
    else:
        binary_tree.left, binary_tree.right = binary_tree.right, binary_tree.left
        invert_binary_tree(binary_tree.left)
        invert_binary_tree(binary_tree.right)

def main():
    node1 = LinkedBinaryTree.LinkedBinaryTree.Node(1)
    node3 = LinkedBinaryTree.LinkedBinaryTree.Node(3)
    node2 = LinkedBinaryTree.LinkedBinaryTree.Node(2, node1, node3)
    node6 = LinkedBinaryTree.LinkedBinaryTree.Node(6)
    node9 = LinkedBinaryTree.LinkedBinaryTree.Node(9)
    node7 = LinkedBinaryTree.LinkedBinaryTree.Node(7, node6, node9)
    root = LinkedBinaryTree.LinkedBinaryTree.Node(4, node2, node7)
    bin_tree = LinkedBinaryTree.LinkedBinaryTree(root)
    rep(bin_tree)
    new = invert_binary_tree()


