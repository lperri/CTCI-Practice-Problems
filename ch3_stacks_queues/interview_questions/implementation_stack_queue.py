# implement stack
# last in -- first out
# needs methods:
#               pop() -- remove
#               push() -- add item to the top
#               peek() -- return the top
#               isEmpty -- returns true only if empty
from typing import Any, List

class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self) -> bool:
        return len(stack) == 0

    def push(self, item: Any) -> List:
        self.stack.append(item)

    def peek(self) -> Any:
        return self.stack[-1]

    def pop(self) -> Any:
        return self.stack.pop() if self.stack else None


class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False

    def peek(self) -> Any:
        return self.queue[0]

    def enqueue(self, item: Any) -> None:
        self.queue.append(item)

    def dequeue(self) -> Any:
        return self.queue.pop(0) if self.queue else None


if __name__ == "__main__":
    stack = Stack()
    stack.push('10')
    stack.push(20)
    stack.push(30)
    print('the next value should be 30 ', stack.peek())
    print('the next value should also be 30 ', stack.pop())
    stack.push(40)
    print('next should be 40 ', stack.pop())
    print('should be false next ', stack.is_empty())

    queue = Queue()
    print('should be true: ', queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    print('should be false: ', queue.is_empty())
    print('peek, should be 1:', queue.peek())
    print('just dequeued this number: ', queue.dequeue())
    print(queue.queue)
