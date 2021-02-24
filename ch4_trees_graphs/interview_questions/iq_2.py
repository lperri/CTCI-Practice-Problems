# minimal tree: Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height
from typing import List
from implementation_tree_graph import *

def create_minimal_height_bst(array: List, start: int, end: int) -> BinaryTreeNode:
    mid_point = (start + end) // 2
    if not array[start:end]:
        return None

    root = BinaryTreeNode(val=array[mid_point])

    root.left = create_minimal_height_bst(
        array, start, (mid_point - 1)
    )
    root.right = create_minimal_height_bst(
        array, (mid_point + 1), end
    )
    return root

if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7]
    print(create_minimal_height_bst(test_list, 0, len(test_list) - 1))