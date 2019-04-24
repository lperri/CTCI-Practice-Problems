# the following code computes the [integer] sqrt of a number. IF the number is not a perfect square (there is no integer square root), then it returns -1. IT does this by trying increasingly large numbers until it finds the right value (or is too high). What is its runtime?

def sqrt(n):
    guess = 1
    while guess*guess <= n:
        if guess*guess == n:
            return guess
        guess += 1
    return -1

""" the answer: runtime of O(SQRT(n)) because guess is the square root of n (if you guess right) so you would never go above it, even if you guess wrong, it would never go above a little over sqrt(n) """
