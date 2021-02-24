# check balanced: implement a function to check if a BT is balanced -- for this Q, balanced is defined by heights of two subtrees never differing by more than 1
from implementation_tree_graph import BinaryTreeNode, BinaryTree

def is_balanced_binary_tree(root: BinaryTreeNode) -> bool:
    if not root:
        return True
    return check_balance(root)

def check_balance(node: BinaryTreeNode) -> bool:
    if node.left:
        height_left = get_height(node.left)
    else:
        height_left = 0
    if node.right:
        height_right = get_height(node.right)
    else:
        height_right = 0
    return abs(height_left - height_right) <= 1

def get_height(node: BinaryTreeNode) -> int:
    if not node:
        return 0
    return max(get_height(node.left), get_height(node.right)) + 1

if __name__ == "__main__":
    tree = BinaryTree(root_val=2)
    node = tree.root
    node.left, node.right = BinaryTreeNode(3), BinaryTreeNode(4)
    node = node.left
    node.left, node.right = BinaryTreeNode(5), BinaryTreeNode(6)
    # node = node.left
    # node.left, node.right = BinaryTreeNode(5), BinaryTreeNode(6)
    print(is_balanced_binary_tree(tree.root))