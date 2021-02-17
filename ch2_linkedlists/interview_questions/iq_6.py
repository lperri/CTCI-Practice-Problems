# check if a linked list is a palindrome
from implementation import *

# def check_palindrome(linked_list: LinkedList) -> bool:
#     ''' use a stack for half elements then compare to other half '''
#     stack = []

#     length_no_head = linked_list.get_length(count_head=False)
#     if length_no_head <= 1:
#         return True

#     # accommodate both odd and even length lists
#     if length_no_head % 2 != 0:
#         is_even = False
#         mid_point = int(length_no_head // 2 + 1)
#     else:
#         is_even = True
#         mid_point = int(length_no_head / 2)

#     # populate stack with first half of list
#     counter = 1
#     curr_node = linked_list.head.next
#     while (is_even and counter <= mid_point) or (not is_even and counter < mid_point):
#         stack.append(curr_node)
#         curr_node = curr_node.next
#         counter += 1

#     # now curr_node is pointing to the middle node if length odd, or the middle-left if even
#     if not is_even:
#         # if it's odd, we want to skip the middle node
#         curr_node = curr_node.next
#     # compare second half of list with elements popped from stack
#     while curr_node:
#         stack_node = stack.pop()
#         if stack_node.val != curr_node.val:
#             return False
#         curr_node = curr_node.next

#     return True

def _copy(linked_list: LinkedList) -> LinkedList:
    copy_list = LinkedList()
    copy_list.head = Node()
    curr_node_copy = copy_list.head
    curr_node_original = linked_list.head.next
    while curr_node_original:
        copy_node = Node()
        copy_node.val = curr_node_original.val
        curr_node_copy.next = copy_node
        curr_node_copy, curr_node_original = curr_node_copy.next, curr_node_original.next
    return copy_list

def _reverse(linked_list: LinkedList) -> LinkedList:
    ''' helper function for reverse strategy -- careful, copy first otherwise will overwrite '''
    # cut off head first -- otherwise you retain a ref to the original head when
    # list gets reversed
    curr_node = linked_list.head.next
    linked_list.head.next = None

    prev_node, curr_node = None, curr_node
    while curr_node is not None:
        actual_next = curr_node.next
        curr_node.next = prev_node
        prev_node, curr_node = curr_node, actual_next

    # create new head and attach to the reversed list
    new_head = Node()
    linked_list.head = new_head
    new_head.next = prev_node
    return linked_list

def check_palindrome(linked_list: LinkedList) -> bool:
    ''' alternative strategy: reverse linked list and compare first halves '''
    reversed = _reverse(_copy(linked_list))
    length_no_head = linked_list.get_length(count_head=False)
    curr_node_reg, curr_node_rev = linked_list.head.next, reversed.head.next
    counter = 1
    while counter <= (length_no_head/2):
        if curr_node_reg.val != curr_node_rev.val:
            return False
        curr_node_reg, curr_node_rev = curr_node_reg.next, curr_node_rev.next
        counter += 1
    return True


# both of these solutions work and are actually the same big O complexity
# time is O(n) where n is the length of the list
# space is O(n) also because we either store half the elements in a stack (O(n/2) = O(n)) or
# we copy the list to reverse it (O(n))
if __name__ == "__main__":
    not_pal_odd = LinkedList()
    not_pal_odd.append(5)
    not_pal_odd.append(4)
    not_pal_odd.append(3)
    not_pal_odd.append(2)
    not_pal_odd.append(1)
    _copy(not_pal_odd).display_as_list()
    # not_pal_odd.display_as_list()
    print('not_pal_odd: ', check_palindrome(not_pal_odd))
    # (_reverse(not_pal_odd).display_as_list())

    is_pal_odd = LinkedList()
    is_pal_odd.append(1)
    is_pal_odd.append(2)
    is_pal_odd.append(3)
    is_pal_odd.append(2)
    is_pal_odd.append(1)
    print('is_pal_odd: ', check_palindrome(is_pal_odd))

    not_pal_even = LinkedList()
    not_pal_even.append(1)
    not_pal_even.append(4)
    not_pal_even.append(3)
    not_pal_even.append(3)
    not_pal_even.append(2)
    not_pal_even.append(1)
    print('not_pal_even: ', check_palindrome(not_pal_even))
    # not_pal_even.display_as_list()
    # (_reverse(not_pal_even).display_as_list())

    is_pal_even = LinkedList()
    is_pal_even.append(1)
    is_pal_even.append(2)
    is_pal_even.append(3)
    is_pal_even.append(3)
    is_pal_even.append(2)
    is_pal_even.append(1)
    print('is_pal_even: ', check_palindrome(is_pal_even))