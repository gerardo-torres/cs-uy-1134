import LinkedBinaryTree

def flatten(root):
    if (root.left is None) and (root.right is None):
        return root
    else:
        if (root.left is None) and (root.right is not None):
            flatten(root.right)
        elif (root.left is not None) and (root.right is None):
            flatten(root.left)
            left = root.left
            root.right = left
            root.left = None
        else:
            flatten(root.left)
            flatten(root.right)
            left = root.left
            right = root.right
            root.right = left
            find_rightmost(left).right = right
            right.parent = find_rightmost(left)
            root.left = None


def find_rightmost(root):
    if root.right is None:
        return root
    else:
        new_root = root.right
        return find_rightmost(new_root)

def main():
    node1 = LinkedBinaryTree.LinkedBinaryTree.Node(1)
    node3 = LinkedBinaryTree.LinkedBinaryTree.Node(3)
    node2 = LinkedBinaryTree.LinkedBinaryTree.Node(2, node1, node3)
    node6 = LinkedBinaryTree.LinkedBinaryTree.Node(6)
    node9 = LinkedBinaryTree.LinkedBinaryTree.Node(9)
    node7 = LinkedBinaryTree.LinkedBinaryTree.Node(7, node6, node9)
    root = LinkedBinaryTree.LinkedBinaryTree.Node(4, node2, node7)
    bin_tree = LinkedBinaryTree.LinkedBinaryTree(root)
    for node in bin_tree.preorder():
        print(node.data)
    flatten(bin_tree.root)
    print("---------")
    for node in bin_tree.preorder():
        print(node.data)

main()
