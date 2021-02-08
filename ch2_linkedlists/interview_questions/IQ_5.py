#2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1s digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list. For ex, 
# (7->1->6) + (5->9->2) = 617 + 295 = 912
# returns (9->1->2) as LL

from problem_2_0 import *

def SumLists(list_1,list_2):
    sum_total = 0
    for list_ in [list_1,list_2]:
        current_node = list_.head
        # start element_num at zero so that the 1s digit won't be multiplied by 10
        element_num = 0
        while current_node.next != None:
            current_node = current_node.next
            sum_total += current_node.data*(10**element_num)
            element_num += 1
    return sum_total

# test
my_list1 = LinkedList()
my_list2 = LinkedList()
my_list1.append(7)
my_list1.append(1)
my_list1.append(6)
my_list2.append(5)
my_list2.append(9)
my_list2.append(2)
print SumLists(my_list1,my_list2)



    
