# Remove Dups: Write code to remove duplicates from an unsorted linked list. FOLLOW UP - how would you solve this problem if a temporary buffer is not allowed? (i.e. must solve probelm in place, not using a temp variable)
from implementation import *

def remove_dups(linked_list: LinkedList) -> LinkedList:
    """ This solution will optimize for runtime and use a set to keep track of dups """
    node_values = set()
    prev_node, curr_node = linked_list.head, linked_list.head.next
    while curr_node != None:
        if curr_node.val in node_values:
            prev_node.next = curr_node.next
        else:
            node_values.add(curr_node.val)
            prev_node = curr_node
        curr_node = curr_node.next
    return linked_list

# def remove_dups(linked_list: LinkedList) -> LinkedList:
#     """ This solution addresses the followup -- if we can't use any other data structures """
#     prev_node, curr_node = linked_list.head, linked_list.head.next
#     while curr_node.next != None:
#         runner_node = curr_node.next
#         while runner_node != None:
#             if runner_node.val == curr_node.val:
#                 prev_node.next = curr_node.next
#                 curr_node = curr_node.next
#             else:
#                 runner_node = runner_node.next
#         prev_node = curr_node
#         curr_node = curr_node.next
#     return linked_list

# first solution (using set) is time O(n) and space O(n)
# second solution is O(n^2) time and O(1) space
if __name__  ==  "__main__":
    my_list = LinkedList()
    my_list.append(22)
    my_list.append(83)
    my_list.append(3)
    my_list.append(83)
    my_list.append(54)
    my_list.append(3)
    my_list.display_as_list()
    remove_dups(my_list)
    my_list.display_as_list()
