# implement a MyQueue class which implements a queue using two stacks
from implementation_stack_queue import Stack
from typing import Any, List

class MyQueue:
    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def _transfer_stack_to_temp_stack(self) -> None:
        while len(self.stack) > 0:
            self.temp_stack.append(self.stack.pop())

    def _transfer_temp_stack_to_stack(self) -> None:
        while len(self.temp_stack) > 0:
            self.stack.append(self.temp_stack.pop())

    def enqueue(self, item: Any) -> None:
        self.stack.append(item)

    def dequeue(self) -> Any:
        self._transfer_stack_to_temp_stack()
        if self.temp_stack:
            item_to_return = self.temp_stack.pop()
        else:
            item_to_return = None
        self._transfer_temp_stack_to_stack()
        return item_to_return

    def is_empty(self) -> bool:
        return (len(self.stack) == 0 and len(self.temp_stack) == 0)

    def peek(self) -> Any:
        self._transfer_stack_to_temp_stack()
        if self.temp_stack:
            first_in_line = self.temp_stack[-1]
        self._transfer_temp_stack_to_stack()
        return first_in_line

if __name__ == "__main__":
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print('should see 1: ', queue.peek())
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    print('should see 1: ', queue.dequeue())
    print('should see 2: ', queue.dequeue())
    print('should see 3: ', queue.dequeue())
    print('should see 4: ', queue.dequeue())
    print('should see 5: ', queue.dequeue())
    print('should see 6: ', queue.dequeue())
    print('should see none: ', queue.dequeue())
