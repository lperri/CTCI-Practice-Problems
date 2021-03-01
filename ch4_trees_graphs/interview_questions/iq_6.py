# successor: writie an agorithm to find the "next" node (i.e. in-order successor) of a given node in a BST
# can assume that each node has a link to its parent
# will also assume no duplicate values

# class BinaryTreeNode:
#     def __init__(self, val: Any = None, left = None, right = None, parent = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.parent = parent

def find_successor_in_bst(node: BinaryTreeNode) -> BinaryTreeNode:
    """
    In-order traversal goes left, current, right
    ALGORITHM:
        - Case 1: node has right subtree
            * go to leftmost node of this subtree and return that node
        - Case 2: node has no right subtree
            * determine if you are on the left or right side of the parent
                * if on left side of parent -> return parent, next in line
                * else if on right side of parent -> that parent is finished,
                so go to its parent & continue until you are at the node which is
                a left child of its parent, then return that parent;
                if this never happens, it means the tree has been fully traversed so
                return None
    """
    if not node:
        return None

    # Case 1
    if node.right:
        # Sub-Case 1.1: node has left subtree
        if node.left:
            while node.left:
                node = node.left
            return node
        # Sub-Case 1.2: node has no left subtree
        return node.right

    # Case 2
    parent = node.parent
    # Sub-Case 2.1: node is the parent's left child
    if node == parent.left:
        return parent
    # Sub-Case 2.2: node is the parent's right child
    else:
        while parent:
            if node == parent.left:
                return parent
            parent = parent.parent
        return None
