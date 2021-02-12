# the following code performs integer division. What is its runtime (assume a and b are both positive)?

def div(a, b):
    count = 0
    sum = b
    while sum <= a:
        sum += b
        count += 1
    return count

# Initial thought is O(a) but the answer: O(a/b) because the number of while loop iterations is O(a/b)
