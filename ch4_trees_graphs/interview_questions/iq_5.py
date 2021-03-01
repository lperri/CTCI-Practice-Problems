# validate BST: check that BST is a BST
from implementation_tree_graph import BinaryTree, BinaryTreeNode

def validate_bst(node: BinaryTreeNode, min_val = None, max_val = None) -> bool:
    """
    I will assume here that there are no duplicate values. Otherwise need to know if they should go left or right.
    ALGORITHM:
        - recursively check that each node is itself a valid BST -- do this by:
            1. verifying the left < curr < right
            2. keeping track of the max and min values seen - checking left side against max, right side against min
    """
    if not node:
        return True
    if min_val and node.val < min_val:
        return False
    if max_val and node.val > max_val:
        return False
    return validate_bst(node.left, min_val=node.val, max_val=max_val) and validate_bst(node.right, min_val=min_val, max_val=node.val)
