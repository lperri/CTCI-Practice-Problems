# first common ancestor
from implementation_tree_graph import BinaryTree, BinaryTreeNode

class Solution:
    def __init__(self):
        self.ancestor = None

    def find_lowest_ancestor(root: BinaryTreeNode, p: BinaryTreeNode, q: BinaryTreeNode) -> bool:
        if not root:
            return False

        curr = root == p or root == q
        left = find_lowest_ancestor(root.left, p, q)
        right = find_lowest_ancestor(root.right, p, q)

        if curr + left + right >= 2:
            self.ancestor = root
        # return True if any eval to true
        return curr or left or right

    def main(root: BinaryTreeNode, p, q) -> BinaryTreeNode:
        find_lowest_ancestor(root, p, q)
        return self.ancestor

# worst case you have to visit every node to find ancestor => O(N)
# space is O(1) - only storing 3 bool vals and one node
