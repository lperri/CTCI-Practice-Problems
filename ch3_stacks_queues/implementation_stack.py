# implement stack
# last in -- first out
# needs methods: 
#               pop() -- remove 
#               push() -- add item to the top
#               peek() -- return the top
#               isEmpty -- returns true only if empty

class Node:
    
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def pop(self):
        if self.top:
            data = self.top.data
            new_top = self.top.next
            self.top = new_top
            return data
        else:
            return 'stack empty'


    def push(self,data):
        if self.top is None:
            self.top = Node(data)
        else:
            new_data = Node(data)
            new_data.next = self.top
            self.top = new_data

    def peek(self):
        return self.top.data 

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

q = Stack()
q.push('10')
q.push(20)
q.push(30)
print 'the next value should be 30'
print q.peek()
print 'the next value should also be 30'
print q.pop()
q.push(40)
print 'next should be 40'
print q.pop()
print 'should be false next'
print q.isEmpty()
