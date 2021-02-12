# the following code computes the [integer] sqrt of a number. IF the number is not a perfect square (there is no integer square root), then it returns -1. IT does this by trying increasingly large numbers until it finds the right value (or is too high). What is its runtime?

def sqrt(n):
    guess = 1
    while guess*guess <= n:
        if guess*guess == n:
            return guess
        guess += 1
    return -1

# O(SQRT(n)) because cane rewrite the while condition as while guess < SQRT(n)
# then guess gets incremented by 1 after each iteration.
# Because we start at guess = 1, we have SQRT(n) iterations total.
