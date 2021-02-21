# stack of plates: implement SetOfStacks, composed of several stacks and
# should create a new stack once the previoius one exceeds capacity.
# SetofStacks.push() and SetOfStacks.pop() should behave like a single stack
# followup: implement popAt(index) which performs pop on a single sub-stack
from typing import List, Any


class SetOfStacks:

    def __init__(self, capacity):
        self.capacity = capacity
        self.all_stacks = []
        self.curr_stack = None
        self.create_stack()

    def create_stack(self, set_curr=True):
        self.all_stacks.append([])
        self.curr_stack = self.all_stacks[-1]

    def is_curr_stack_empty(self) -> bool:
        return len(self.curr_stack) == 0:

    def push_to_stack(self, item: Any) -> List:
        if len(self.curr_stack) == self.capacity:
            self.create_stack()
        self.curr_stack.append(item)

    def pop_from_stack(self) -> Any:
        if self.is_curr_stack_empty():
            self.all_stacks.pop()
            if self.all_stacks:
                self.curr_stack = self.all_stacks[-1]
        return self.curr_stack.pop()


if __name__ == "__main__":
    set_of_stacks = SetOfStacks(capacity=3)
    print(set_of_stacks.all_stacks)
    set_of_stacks.push_to_stack(10)
    print(set_of_stacks.all_stacks)
    set_of_stacks.push_to_stack(20)
    print(set_of_stacks.all_stacks)
    set_of_stacks.push_to_stack(30)
    print(set_of_stacks.all_stacks)
    set_of_stacks.push_to_stack(40)
    print(set_of_stacks.all_stacks)
    print('pop 40: ', set_of_stacks.pop_from_stack())
    print(set_of_stacks.all_stacks)
    print('pop 30: ', set_of_stacks.pop_from_stack())
    set_of_stacks.push_to_stack(9)
    print(set_of_stacks.all_stacks)