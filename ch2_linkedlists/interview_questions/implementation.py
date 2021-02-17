class Node:
    def __init__(self, val=None):
        ''' constructor containing the data in a given node and a pointer to the next node (if a next node exists) '''
        self.val = val
        self.next = None

class LinkedList:
    ''' wraps Node class; useful because if head node changes for one obj, other objs can continue to reference their head node '''
    def __init__(self):
        ''' constructor containing only a head node -- head node contains no data (in this implementation)'''
        self.head = Node()

    def prepend(self, val) -> None:
        ''' prepend a node to the start of the linked list '''
        current_first = self.head.next
        new_node = Node(val)
        self.head.next = new_node
        new_node.next = current_first


    def append(self, val) -> None:
        ''' append a node to the end of the linked list '''
        # start at head node
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        # now at the end of the linked list
        new_node = Node(val)
        current_node.next = new_node

    def remove(self, target_val) -> None:
        ''' removes node if exists with value=target_val '''
        prev_node, current_node = self.head, self.head.next
        while current_node.next != None:
            if current_node.val == target_val:
                prev_node.next = current_node.next
            prev_node, current_node = current_node, current_node.next

    def get_length(self, count_head=True) -> int:
        ''' obtain length of linked list by traversing elements and counting them '''
        # set counter at 1 to account for head node
        current_node = self.head
        counter = 1 if count_head else 0
        while current_node.next != None:
            counter += 1
            current_node = current_node.next
        return counter

    def display_as_list(self) -> None:
        ''' prints node values in list format '''
        elements = []
        current_node = self.head
        while current_node != None:
            elements.append(current_node.val)
            current_node = current_node.next
        print(elements)
