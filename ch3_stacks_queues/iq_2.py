# stack min -- design a stack which, in addition to push and pop, has a function `min`
# which returns the min element -- all O(1) operations
from typing import List

class Stack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, item: [int, float]) -> List:
        self.stack.append(item)
        if item < self.min:
            self.min = item

    def pop(self) -> [int, float]:
        return self.stack.pop() if len(self.stack) > 0 else None

    def min_value(self) -> [int, float]:
        return self.min


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print('the next value should be 30 ', stack.pop())
    stack.push(40)
    print('min is ', stack.min_value())
