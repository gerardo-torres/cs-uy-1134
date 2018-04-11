class BinarySearchTreeMap:
    class Item:
        def __init__(self, key, value=None):
            self.item = item
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def __getitem__(self, key):
        node = self.subtree_find(key)
        if node is not None:
            return node.item.value
        else:
            raise KeyError("Key Error: " + str(key))

    def subtree_find(self, key):
        curr = self.root
        while curr is not None:
            if curr.item.key == key:
               return curr
            elif curr.item.key < key:
                curr.right
            else:
                curr.left 
        return None

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass    

