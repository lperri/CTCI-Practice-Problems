# You are looking for a specific value in a binary tree, but the tree is not a binary search tree. What is the time complexity of this?

"""
First: difference between binary tree and binary search tree

-- search tree has the property that for any node the right node greater than current, and left smaller than current
-- regular binary trees don't have this sorting property.

Answer: because there is no order to the tree, this would take O(n) to find a specific node.
In other words, you may have to visit every single node to find the value.
"""
