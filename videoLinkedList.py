''' Credit for some of the methods:  https://www.youtube.com/watch?v=JlMyYuY1aXU&t=322s '''

class Node:
    
    def __init__(self, data_value=None):
        self.data_value = data_value
        self.next_value = None
# user never interfaces with Node class -- just a subclass of LinkedList


class LinkedList:
    
    def __init__(self):
        # head node will never contain any actual data -- not a data node
        # user will not be able to access head node, but acts as a placeholder to allow us to point to the first element in the list
        self.head_node = Node()

    def append(self,data_value):
        new_node = Node(data_value)
        # start at leftmost node, i.e. head
        current_node = self.head_node
        # while the node value is not None (i.e. we're not yet at the last node)
        while current_node.next_value != None:
        # set the current node to the next one i.e. traverse through list
            current_node = current_node.next_value
        # finally, we're out of the while loop so we have reached the last node, and now we need to add the new node to the end of the list
        current_node.next_value = new_node

    def length(self):
        current_node = self.head_node
        total = 0
        while current_node.next_value != None:
            total += 1
            current_node = current_node.next_value
        return total

    def display(self):
        elements = []
        current_node = self.head_node
        while current_node.next_value != None:
            current_node = current_node.next_value
            elements.append(current_node.data_value)
        print elements

    def deleteElement(self,position):
        ''' for ex: delete the 5th element in SLL, user would input index=5 '''
        # first check to make sure index is not greater than length
        if position > self.length():
            return 'position is greater than length of linked list. Run [your list].length() to obtain this length'

        elif position == 0:

        # start at the head node
        current_node = self.head_node
        # set up counter to keep track of the position i.e. number of node
        # note position starts at 0 because head node doesn't contain data
        element_num = 0
        while element_num < position:
            current_node = current_node.next_value
            element_num += 1
        next_node = current_node.next_value
        next_next_node = next_node.next_value
        current_node.next_value = next_next_node







# test:
mylist = LinkedList()
mylist.append(1)
mylist.append(55)
mylist.append(22)
mylist.append(3)
mylist.display()
mylist.deleteElement(2)
mylist.display()
