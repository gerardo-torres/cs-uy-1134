import LinkedBinaryTree

def invert_bt(binary_tree):
    new_root = invert_bt_helper(bt.root)
    return LinkedBinaryTree(new_root)  # building the tree from the bottom up

def invert_bt_helper(node):  
    if node is None:
        return None
    else:
        new_left = invert_bt_helper(node.right)
        new_right = invert_bt_helper(node.left)
        new_node = LinkedBinaryTree.Node(node.data, new_left, new_right)
        return new_node

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
    new = invert_bt()
