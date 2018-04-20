def is_bst(binary_tree):
    return is_bst_helper(binary_tree.root)[0]

def is_bst_helper(curr_root):
    """ recursive function that returns (boolean, (min, max)) """
    if (curr_root.left is None) and (curr_root.right is None):
        curr_val = curr_root.data
        return (True, (curr_val, curr_val))  # return tuple
    else:
        if (curr_root.left is None) and (curr_root.right is not None):
            boolean = curr_root.data < curr_root.right.data
            right = is_bst_helper(curr_root.right)
            my_min = min(right[1][0], curr_root.data)
            my_max = max(right[1][1], curr_root.data)
            my_boolean = boolean and right[0]
            return (my_boolean, (my_min, my_max))  # return tuple
            
        elif (curr_root.left is not None) and (curr_root.right is None):
            boolean = curr_root.left.data < curr_root.data
            left = is_bst_helper(curr_root.left)
            my_min = min(left[1][0], curr_root.data)
            my_max = max(left[0][1], curr_root.data)
            my_boolean = boolean and left[0]
            return (my_boolean, (my_min, my_max))  # return tuple

        else:  # both left and right have values
            left = is_bst_helper(curr_root.left)
            right = is_bst_helper(curr_root.right)
            my_min = min(left[1][0], right[1][0], curr_root.data)
            my_max = max(left[1][1], right[1][1], curr_root.data)
            boolean = curr_root.left.data < curr_root.data < curr_root.right.data
            my_boolean = boolean and right[0] and left[0]
            return (my_boolean, (my_min, my_max))  # return tuple

def main():
    """ create a BST """
    bst = pass
