# the following code computes a^b. What is its runtime?

def power(a: int, b: int):
    if b < 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a * power(a, (b - 1))

# For a recursive function even when each call is O(1), you have to think about the number of calls to that function that are made.
# Here we make O(b) calls, because we multiply a by itself b times to get a^b
