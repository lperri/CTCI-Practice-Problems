# check if two linked lists intersect
from implementation import *

def intersection_node(list1: LinkedList, list2: LinkedList) -> [Node, bool]:
    # observe that lists that intersect will always have the same last node
    # check this property first
    curr1, curr2 = list1.head.next, list2.head.next
    while curr1:
        curr1 = curr1.next
    while curr2:
        curr2 = curr2.next
    # at this point, curr1 and curr2 should point to the same node - if not, return False
    if curr1 != curr2:
        return False

    # the above test passed, so now find the intersection point
    # first make sure to start the lists in sync (same num of nodes til the end)
    # => deal with length difference
    length1, length2 = list1.get_length(count_head=False), list2.get_length(count_head=False)
    length_diff = length2 - length1

    if abs(length_diff) > 0:
        counter = 0
        curr1, curr2 = list1.head.next, list2.head.next
        while counter < length_diff:
            if length_diff > 0:
                # list2 is longer
                curr2 = curr2.next
            elif length_diff < 0:
                # list1 is longer
                curr1 = curr1.next
            counter += 1

    # now they should be in sync
    while curr1 and curr2:
        if curr1 == curr2:
            return curr1
        curr1, curr2 = curr1.next, curr2.next
    return False

if __name__ == "__main__":
    l1_node1 = Node(val=5)
    l2_node1 = Node(val=6)
    l2_node1.next = Node(val=7)
    l2_node1.next.next = Node(val=8)
    # l1_node1.next = l2_node1.next.next

    list1 = LinkedList()
    list1.head.next = l1_node1
    list2 = LinkedList()
    list2.head.next = l2_node1

    list1.display_as_list()
    list2.display_as_list()

    print(intersection_node(list1, list2))
