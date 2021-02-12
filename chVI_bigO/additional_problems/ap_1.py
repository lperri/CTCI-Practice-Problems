# The following code computes the product of a and b. What is its runtime?

def product(a: int, b: int) -> int:
    sum = 0
    # note that in python3, range ~ xrange i.e. O(1)
    for i in range(b):
        sum += a
    return sum

""" the answer: the runtime of this code is O(b) """
