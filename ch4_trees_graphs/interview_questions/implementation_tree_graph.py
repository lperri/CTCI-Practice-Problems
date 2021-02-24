from typing import Any, List

class BinaryTreeNode:
    def __init__(self, val: Any = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root_val = None):
        self.root = BinaryTreeNode(root_val)

    def pre_order_traversal(self):

        def traverse(node):
            if not node:
                return
            # process node somehow
            print(node.val)
            traverse(node.left)
            traverse(node.right)

        node = self.root
        return traverse(node)

    def in_order_traversal(self):
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            # process node somehow
            print(node.val)
            traverse(node.right)

        node = self.root
        return traverse(node)

    def post_order_traversal(self):
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            # process node somehow
            print(node.val)

        node = self.root
        return traverse(node)

class NaryTreeNode:
    def __init__(self, val: Any = None):
        self.val = val
        self.children = []

    def add_child(self, new_child) -> None:
        self.children.append(new_child)

class GraphNode:
    def __init__(self, val: Any = None, marked: bool = False):
        self.val = val
        self.marked = marked
        self.neighbors = []

    def add_neighbors(self, *new_neighbors) -> None:
        for neighbor in new_neighbors:
            self.neighbors.append(neighbor)
