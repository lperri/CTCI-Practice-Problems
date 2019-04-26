from problem_2_0 import *

# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list. FOLLOW UP - how would you solve this problem if a temporary buffer is not allowed? (i.e. must solve probelm in place, not using a temp variable)

def removeDups(linked_list):
    # start at head node
    current_node = linked_list.head
    # while we are not at the end of the list,
    while current_node.next != None:
        # set runner to current
        runner_node = current_node
        # while we are not at the end of the list,
        while runner_node.next != None:
            # check if node that runner points to is the same as current value
            if runner_node.next.data == current_node.data:
                # if it is, set runner node's pointer to move to skip over 
                runner_node.next  = runner_node.next.next
            else:
                # otherwise, just move runner to the next node
                runner_node = runner_node.next
        # set current to the next node once you've looped over all future nodes
        current_node = current_node.next
    # return modified linked list
    return linked_list

# test:
my_list = LinkedList()
my_list.append(22)
my_list.append(83)
my_list.append(3)
my_list.append(83)
my_list.append(54)
my_list.append(3)
my_list.displayAsList()
removeDups(my_list)
my_list.displayAsList()
