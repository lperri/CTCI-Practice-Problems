# list of depths: given a binary tree, design an algorithm that creates a linked list of all the nodes at each depth
from typing import Any, List
from implementation_tree_graph import BinaryTreeNode


# use a list of linked lists (LLs) where each level's nodes is an entry (a LL) in the array

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item: Any) -> None:
        self.queue.append(item)

    def dequeue(self) -> Any:
        return self.queue.pop(0)

    def peek(self) -> Any:
        return self.queue[0]

    def is_empty(self) -> bool:
        return len(self.queue) == 0


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if self.head:
            curr = self.head
            while curr:
                prev = curr
                curr = curr.next
        else:
            self.head = LinkedListNode(val=val)


class LinkedListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next


# implement a pre-order traversal
def create_depth_lists(
    node: BinaryTreeNode,
    list_of_linked_lists: List[LinkedList] = [],
    depth: int = 0
) -> None:
    """
    Keep track of the depth on each recursive call
    ALGORITHM:
        - if the LL for depth X has not been created yet, make the node the head of LL for that depth
        - if the depth exists, append new node to the end of the LL
    """
    # base case
    if not node:
        return

    if depth != 0 and len(list_of_linked_lists) > depth:
        # LL already exists for that depth => append
        ll_node = list_of_linked_lists[depth].head
        while ll_node:
            prev = ll_node
            ll_node = ll_node.next
        prev.next = LinkedListNode(val=node.val)
    else:
        # create a new LL with curr node as head
        new_linked_list = LinkedList()
        new_linked_list.head = LinkedListNode(val=node.val)
        list_of_linked_lists.append(new_linked_list)

    # then call again for the next depth, left and right children of node
    create_depth_lists(node.left, list_of_linked_lists, depth + 1)
    create_depth_lists(node.right, list_of_linked_lists, depth + 1)

    return list_of_linked_lists


# implement a level-by-level traversal
def create_depth_lists(node: BinaryTreeNode) -> List[LinkedList]:
    result = []
    current = LinkedList()

    if node:
        # set the root as head of first LL
        current.head = node

    while current.head:
        # append previous level's resulting LL to result
        result.append(current)
        # current now become parents
        parents = current
        # instantiate a new LL for the new level
        current = LinkedList()
        # iterate through parents' children, building that level's list
        for parent in parents:
            if parent.left:
                current.append(LinkedListNode(val=parent.left.val))
            if parent.right:
                current.append(LinkedListNode(val=parent.right.val))

    return results
