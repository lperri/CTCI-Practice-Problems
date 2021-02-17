# delete a node in the middle (any node other than first and last) given ONLY access to THAT node
from implementation import *

def delete_a_middle_node(node: Node) -> None:
    ''' strategy: shift the rest of the linked list (using values) back by one, thus deleting this node '''
    rest_of_list_values = []
    node_to_delete = node

    # collect values we want to keep
    curr_node = node_to_delete.next
    while curr_node != None:
        rest_of_list_values.append(curr_node.val)
        curr_node = curr_node.next

    # now push values left
    # and remove the last node (we have one less node now; last node has dup value to the one before)
    curr_node = node_to_delete
    prev_node = curr_node
    i = 0
    while curr_node.next != None:
        curr_node.val = rest_of_list_values[i]
        i += 1
        prev_node, curr_node = curr_node, curr_node.next
    # now prev_node is the node before last, so link it to None => removing the last node
    prev_node.next = None

# time O(n) space O(1)
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(5)
    my_list.append(4)
    my_list.append(3)
    my_list.append(2)
    my_list.append(1)
    node_to_delete = my_list.head.next.next
    my_list.display_as_list()
    delete_a_middle_node(node_to_delete)
    my_list.display_as_list()
