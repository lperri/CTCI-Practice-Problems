# the following code performs integer division. What is its runtime (assume a and b are both positive)?

def div(a,b):
    count = 0
    sum = b
    while sum <= a:
        sum += b
        count += 1
    return count

""" the answer: O(a/b) *be careful! b matters!*
"""
