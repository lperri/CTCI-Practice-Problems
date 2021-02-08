# If a binary search tree is not balanced, how long might it take (worst case) to find an element in it?

""" 
First: what is a tree? It is a data structure.

Components of a binary tree:
-- root: a tree only has one root, primary node
-- child: the root in a binary tree has two children and they themselves have children
    -- each node left and right has 2 children (can be null)
-- a leaf is a node at the bottom of the tree i.e. it has NO children


Next: what is a binary search tree?
    
    A binary search tree is a node-based binary tree data structure which fulfills a specific ordering property.

    *The left subtree of a node contains nodes with keys < the node's key
    *The right subtree contains ndoes with keys > the node's key
    *The left and right subtree must also be binary search trees
    *No duplicate nodes allowed


Balanced VS Unbalanced Trees:
    -- balanced: no leaf node that is more than one level away than any other leaf node; the difference in depth between any two leaf nodes is at most 1.



answer to question: If it's not balanced, then it's basically a 1 branch long list of sorted elements, so worst case it would take O(n) where n is the number of nodes. """
