# Heaps
*4/30/2018*

## Priority Queues
### Data Model:
A collection of a priority-value pairs. that come out in an increasing priorities order.  
Two implementations:  
- minimum priority queue: come out in a decreasing order
- maximum priority queue: come out in an increasing order  

## Heap:
Let T be a binary tree. We say that T is a Heap if it satisfies:
- Heap order property: in every node n in T, the priority in n is less than or equal to the priorities in n's children
- Nearly-complete property: if h is the height of the tree, then all levels: have the maximum number of nodes possible (that is level i has 2^i nodes), and the remaining nodes, at level h reside in the leftmost possible position.