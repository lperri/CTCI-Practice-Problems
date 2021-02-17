# partition: partition a linked list around a value x
# such that all nodes less than x come before all nodes greater than or equal to x
# important: the parition element x can appear anywhere in the "right partition"
# it does not need to appear between the left and right partitions
from implementation import *

def partition(linked_list: LinkedList, partition_val: int) -> LinkedList:
    """
        explanation of algorithm:
        -   iterate through list using two runners
        -   "first half runner" starts at beginning only going up to middle
        -   "second half runner" starts at the middle goes to end
        -   if the "first half runner" finds a node whose val < partition,
        iterate through second half using the "second half runner" and swap
    """
    first_half_runner = linked_list.head.next
    length = linked_list.get_length(count_head=False)
    if length <= 1:
        return linked_list

    counter = 1
    curr_node = linked_list.head.next
    while counter <= (length/2):
        curr_node = curr_node.next
        counter += 1
    # now curr_node points to where we want second half runner to start
    second_half_runner = curr_node

    while second_half_runner != None and first_half_runner != second_half_runner:
        if first_half_runner.val >= partition_val and second_half_runner.val < partition_val:
            # swap values because both are in wrong place
            first_half_runner.val, second_half_runner.val = \
                second_half_runner.val, first_half_runner.val
            # then advance both
            first_half_runner, second_half_runner = first_half_runner.next, second_half_runner.next
        elif first_half_runner.val >= partition_val and second_half_runner.val >= partition_val:
            # first is in wrong place but second is not, so advance second
            second_half_runner = second_half_runner.next
        elif first_half_runner.val < partition_val and second_half_runner.val >= partition_val:
            # both in correct place, advance both
            first_half_runner, second_half_runner = first_half_runner.next, second_half_runner.next
        elif first_half_runner.val < partition_val and second_half_runner.val <= partition_val:
            # second is in wrong place but first is not, so advance first
            first_half_runner = first_half_runner.next

    return linked_list


# O(n) time and O(1) space
if __name__ == "__main__":
    list1 = LinkedList()
    list1.append(2)
    list1.append(3)
    list1.append(6)
    list1.append(1)
    list1.display_as_list()
    partition(list1, 2).display_as_list()



    list2 = LinkedList()
    list2.append(2)
    list2.append(2)
    list2.append(32)
    list2.append(12)
    list2.append(3)
    list2.append(6)
    list2.append(1)
    list2.display_as_list()
    partition(list2, 6).display_as_list()