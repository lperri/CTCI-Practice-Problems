# 2.2 Return Kth to last: implement an algorithm to find the kth to last element of a singly linked list
from implementation import *

def get_kth_to_last_element(linked_list: LinkedList, k: int):
    ''' obtain kth-to-last element by first obtaining length, then traversing up to the desired index '''
    length = linked_list.get_length()
    current_node = linked_list.head
    index_kth_to_last = length - k
    if k < 0:
        raise ValueError('Enter a positive value for k')
    elif k >= length:
        raise ValueError('Enter a value for k that is smaller than the length of the linked list')
    i = 0
    while i < index_kth_to_last:
        current_node = current_node.next
        i += 1
    return current_node.val


# time complexity = O(n), space O(1)

if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(22)
    my_list.append(83)
    my_list.append(3)
    my_list.append(45)
    my_list.append(12)
    my_list.get_length()

    # test of get_kth_to_last_element(linked_list)
    print('the following answer should be 83: ', get_kth_to_last_element(my_list,4))
    print('the following answer should be 22: ', get_kth_to_last_element(my_list,5))
    # print('should be error: ', get_kth_to_last_element(my_list,-3))
    print('should be error: ', get_kth_to_last_element(my_list,7))
