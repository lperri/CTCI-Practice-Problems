# find cycle if exists in a list
from implementation import *

def detect_loop(linked_list: LinkedList) -> Node:
    """ return first node in loop if loop exists, otherwise return None
        - the fast and slow runners intersect at K % L nodes away from the start
        (where K = number nodes before the start of cycle, L = number of nodes in cycle)
        - strategy: set off a new runner from the head, keeping one at the intersection node
        - we don't know either of these numbers, but we do know that the head is now at the same distance
        from the starting cycle node as the intersection node => when they meet => return node
    """
    fast, slow = linked_list.head.next, linked_list.head.next
    while fast and slow:
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            # now we have found the point of intersection inside the loop
            intersection = slow
            break
    if not intersection:
        return None

    new_runner = linked_list.head.next
    while new_runner != slow:
        new_runner, slow = new_runner.next, slow.next
    return new_runner


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head.next = Node(val="hey")
    node1 = linked_list.head.next
    node1.next = Node(val="hi")
    node2 = node1.next
    node2.next = Node(val=201)
    node3 = node2.next
    node3.next = Node(val=13)
    node4 = node3.next
    node4.next = node2

    print(detect_loop(linked_list).val)
