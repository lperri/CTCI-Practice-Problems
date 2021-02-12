# The following code computes a%b. What is its runtime?
def mod(a: int, b: int) -> int:
    if b <= 0:
        return -1
    div = a / b
    return a - (div * b)

""" answer: the runtime is constant, O(1) """
