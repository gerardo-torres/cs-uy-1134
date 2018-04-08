# Vitamins - 4/6/18

1. 
Draw the state of the linked list object as the following code executes:

```
from DoublyLinkedList import *
L = DoublyLinkedList()
L.add_first(1)
L.add_last(3)
L.add_last(5)
L.add_after(L.first_node(),2)
L.add_before(L.last_node(),4)
L.delete_node(L.last_node())
L.add_first(0)
print(L)
```
What is the output of the code?

> 0 <-> 1 <-> 2 <-> 3 <-> 4

2. 
Draw the state of the deque object as the following code executes:
```
from ​ArrayDeque import ​*
D = ArrayDeque()
D.add_first(3)
D.add_last(4)
D.add_first(2)
D.add_last(5)
D.add_first(1)
D.delete_last()
D.add_first(0)
```

> 0, 1, 2, 3, 4 