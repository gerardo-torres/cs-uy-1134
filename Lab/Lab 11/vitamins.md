1. Given the following binary tree:
- Give the postorder, preorder, and inorder traversals of the tree?  
ans:  
post: (LRD)  
D, B, G, E, F, C, A  
pre: (DLR)  
F, G, E, C, D, B, A  
in: (LDR)  
B, D, A, G, E, C, F  
- What is the total height of the tree?
ans: 3
- What is the depth of node E? 
ans: 3

2. Written on paper

3. Give each function a meaningful name. You may find it helpful to trace the execution of this code. Think about the different sizes and shapes of trees possible.

- a.
    ```python
        def ​mystery(root):
            ​if ​root ​is None​:
            ​   return ​0
            ​elif ​root.left ​is None and ​root.right ​is None​:
            ​   return ​1
            ​return ​mystery(root.left) + mystery(root.right)
    ```
    ans: number_of_nodes(root)

- b.

    ```python
        def ​mystery(p, q):
            if ​p is not None and ​q is not None​:
                return ​(p.data == q.data) and ​\
                    mystery(p.left, q.left) and \
                    mystery(p.right, q.right)
            return ​p is ​q
    ```
    ans: check_if_equal(root)

4. Written on paper.