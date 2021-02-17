# Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1s digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list. For ex,
# (7->1->6) + (5->9->2) = 617 + 295 = 912
# returns (9->1->2) as LL
from implementation import *

def sum_reversed_lists(list1: LinkedList, list2: LinkedList) ->  LinkedList:
    curr_node_1, curr_node_2 = list1.head.next, list2.head.next
    # create new linked list to store result
    sum_list = LinkedList()
    curr_node_sum_list = sum_list.head

    carry = 0
    while curr_node_1 or curr_node_2:

        if curr_node_1 and curr_node_2:
            sum_vals = curr_node_1.val + curr_node_2.val
            # deal with carry -- if sum_vals = 14, 4 is the digit we hold and carry 1
            if sum_vals >= 10:
                sum_vals, new_carry = sum_vals % 10, 1
            else:
                new_carry = 0
            curr_node_1, curr_node_2, curr_node_sum_list.next, carry = curr_node_1.next, curr_node_2.next, Node(val=(sum_vals + carry)), new_carry

        elif curr_node_1 and not curr_node_2:
            curr_node_1, curr_node_sum_list.next = curr_node_1.next, Node(val=(curr_node_1.val + carry))

        else:
            curr_node_2, curr_node_sum_list.next = curr_node_2.next, Node(val=(curr_node_2.val + carry))

        curr_node_sum_list = curr_node_sum_list.next
    return sum_list

# the reason why it's an easier problem to have the digits in reverse order is because
# if the lists are different lengths, the nodes will still be aligned correctly

def pad_zeroes(linked_list: LinkedList, desired_length: int) -> LinkedList:
    while linked_list.get_length(count_head=False) < desired_length:
        linked_list.prepend(0)
    return linked_list

def sum_forward_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    # get length and pad with zeroes if length1 != length2
    length1, length2 = list1.get_length(count_head=False), list2.get_length(count_head=False)
    if length1 < length2:
        list1 = pad_zeroes(list1, length2)
    elif length2 < length1:
        list2 = pad_zeroes(list2, length1)

    # create and initialize new linked list to store result
    sum_list = LinkedList()
    prev_node_sum_list = sum_list.head

    # iterate through each list and sum values
    curr_node_1, curr_node_2 = list1.head.next, list2.head.next
    carry = 0
    while curr_node_1 and curr_node_2:
        sum_vals = curr_node_1.val + curr_node_2.val

        if sum_vals >= 10:
            sum_vals, carry = sum_vals % 10, 1
        else:
            carry = 0

        curr_node_sum_list = Node(val=sum_vals)
        prev_node_sum_list.next = curr_node_sum_list

        if prev_node_sum_list.val:
            prev_node_sum_list.val += carry

        curr_node_1, curr_node_2, prev_node_sum_list = curr_node_1.next, curr_node_2.next, curr_node_sum_list

    return sum_list


if __name__ ==  "__main__":
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)

    list2 = LinkedList()
    list2.append(9)
    list2.append(9)
    # sum_reversed_lists(list1, list2).display_as_list()
    sum_forward_lists(list1, list2).display_as_list()
