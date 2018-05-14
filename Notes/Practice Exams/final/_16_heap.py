class Empty(Exception):
    pass

class ArrayMinHeap:
    class Item:
        def __init__(self, priority, value=None):
            self.priority = priority
            self.value = value

        def __lt__(self, other):
            return self.priority < other.priority


    def __init__(self, priorities_lst=None, values_lst = None):
        self.data = [None]
        # add later
        if(priorities_lst is not None):
            for i in range(len(priorities_lst)):
                self.data.append(ArrayMinHeap.Item(priorities_lst[i], values_lst[i]))
            first_non_leaf_ind = self.parent(len(self.data) - 1)
            for i in range(first_non_leaf_ind, 0, -1):
                self.fix_down(i)


    def __len__(self):
        return len(self.data) - 1

    def is_empty(self):
        return len(self) == 0


    def left(self, j):
        return 2*j

    def right(self, j):
        return 2*j+1

    def parent(self, j):
        return j // 2


    def has_left(self, j):
        return self.left(j) <= len(self.data) - 1

    def has_right(self, j):
        return self.right(j) <= len(self.data) - 1


    def min(self):
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        item = self.data[1]
        return (item.priority, item.value)


    def insert(self, priority, value=None):
        self.data.append(ArrayMinHeap.Item(priority, value))
        self.fix_up(len(self.data) - 1)


    def delete_min(self):
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        self.swap(1, len(self.data) - 1)
        item = self.data.pop()
        self.fix_down(1)
        return (item.priority, item.value)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def fix_up(self, j):
        parent_ind = self.parent(j)
        if (j > 1 and self.data[j] < self.data[parent_ind]):
            self.swap(j, parent_ind)
            self.fix_up(parent_ind)

    def fix_down(self, j):
        if (self.has_left(j)):
            left = self.left(j)
            small_child = left
            if (self.has_right(j)):
                right = self.right(j)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self.data[small_child] < self.data[j]:
                self.swap(j, small_child)
                self.fix_down(small_child)


def heap_sort(lst):
    n = len(lst)
    heap = ArrayMinHeap(lst, [None]*n)
    res_lst = []
    while (heap.is_empty() == False):
        (priority, value) = heap.delete_min()
        res_lst.append(priority)
    return res_lst


srt_lst = heap_sort([5, 2, 7, 6, 10, 1, 3, 8, 0, 4])
print(srt_lst)