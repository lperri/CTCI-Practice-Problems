class Node:
    def __init__(self, data=None):
        ''' constructor containing the data in a given node and a pointer to the next node (if a next node exists) '''
        self.data = data
        self.next = None

class LinkedList:
    ''' wraps Node class; useful because if head node changes for one obj, other objs can continue to reference their head node '''
    def __init__(self):
        ''' constructor containing only a head node -- by def., head node contains no data '''
        self.head = Node()

    def append(self,data):
        # start at head node
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        # now at the end of the linked list
        new_node = Node(data)
        current_node.next = new_node

    def displayAsList(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print elements

# test:
#my_list = LinkedList()
#my_list.append(22)
#my_list.append(83)
#my_list.append(3)
#my_list.append(54)
#my_list.displayAsList()

