
class OpenAddressingHashMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value
    
    def __init__(self):
        '''Put any useful member variable here. Suggestions: Capacity N,
        size of the hash table n'''
        self.N = 7
        self.size = 0
        self.table = [None] * self.N
    
    def __len__(self):
        '''Returns the number of elements in the map'''
        return self.size
    
    def is_empty(self):
        '''Returns whether the map is empty or not'''
        return self.size == 0
    
    def __getitem__(self, k):
        '''Finds the key k in the table. And returns the value associated with key k. 
        If key not found, raises a KeyError'''
        for item in self.data:
            if item.key == k:
                return item.value
        raise KeyError("KeyError")
        
    def __setitem__(self, k, v):
        i = hash(k) % self.N
        while self.table[i] != None:
            if self.table[i] != "Used" and self.table[i].key == k:
                return self.table[i].value
            i = (i + 1) % self.N
        raise KeyError("invalid key!")
    
    def __delitem__(self, k):
        '''Finds the key k in index j and marks it as available
        (vacated)'''
    
    def __iter__(self):
        '''Iterates through the bucket array'''
        
    
    def rehash(self, new_size):
        '''Updates the capacity of the bucket array; reinserts
        everything'''
