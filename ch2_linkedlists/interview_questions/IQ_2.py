# 2.2 Return Kth to last: implement an algorithm to find the kth to last element of a singly linked list

from problem_2_0 import *

def getLength(linked_list):
    ''' obtain length of linked list by traversing elements and counting them '''
    # set counter at 1 to account for head node
    current_node = linked_list.head
    counter = 1
    while current_node.next != None:
        counter += 1
        current_node = current_node.next
    return counter

def getKthToLastElement(linked_list,k):
    ''' obtain kth-to-last element by first obtaining length, then traversing up to the desired index '''
    length = getLength(linked_list)
    current_node = linked_list.head
    index_kth_to_last = length - k
    if k < 0:
        return 'Please enter a positive value for k.'
    elif k >= length:
        return 'Sorry, {}th-to-last element does not exist in the linked_list. Enter a value for k that is smaller than the length of the linked list.'.format(k)
    else:
        i = 0
        while i < index_kth_to_last:
            current_node = current_node.next
            i += 1
        return current_node.data



# test of getLength(linked_list)
my_list = LinkedList()
my_list.append(22)
my_list.append(83)
my_list.append(3)
my_list.append(45)
my_list.append(12)
#getLength(my_list)

# test of getKthToLastElement(linked_list)
#print 'the following answer should be 83' 
#print getKthToLastElement(my_list,4)
#print 'the following answer should be 22'
#print getKthToLastElement(my_list,5)
#print 'should be error'
#print getKthToLastElement(my_list,-3)
#print 'should be error'
#print getKthToLastElement(my_list,7)


