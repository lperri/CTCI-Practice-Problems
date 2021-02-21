# sort stack: sort a stack such that the smallest items are on top - you can use an additional temp stack
from typing import Any, List

class SortStack:
    def __init__(self):
        self.sorted_stack = []
        self.temp_stack = []

    def push(self, item: Any) -> None:
        if self.sorted_stack and self.sorted_stack[-1] >= item:
            self.sorted_stack.append(item)
        else:
            # move all smaller items to the temp stack
            while self.sorted_stack and self.sorted_stack[-1] < item:
                self.temp_stack.append(self.sorted_stack.pop())
            # now place the item in the sorted stack
            self.sorted_stack.append(item)
            # now move all the smaller items back to the sorted stack
            while len(self.temp_stack) > 0:
                self.sorted_stack.append(self.temp_stack.pop())


    def pop(self) -> Any:
        return self.sorted_stack.pop()

    def peek(self) -> Any:
        return self.sorted_stack[-1]

    def is_empty(self) -> bool:
        return (len(self.sorted_stack) == 0) and (len(self.temp_stack) == 0)

if __name__ == "__main__":
    stack = SortStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print('the next value should be 10 ', stack.peek())
    print('the next value should also be 10 ', stack.pop())
    stack.push(5)
    stack.push(203)
    print('next should be 5 ', stack.pop())
    print('should be false next ', stack.is_empty())