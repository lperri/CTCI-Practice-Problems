# The following code computes the [integer] square root of a number. If the number is not a perfect square (there is no integer square root), then it returns -1. It does this by successive guessing. If n is 100, it first guesses 50. Too high? Try something lower -- halfway between 1 and 50. What is its runtime?

def sqrt(n):
    return sqrt_helper(n,1,n)

def sqrt_helper(n,int_min,int_max):
    if int_max < int_min:
        return -1
    guess = (int_min + int_max)/2
    if guess**2 == n:
        return guess
    elif guess**2 < n:
        return sqrt_helper(n,guess+1,int_max)
    else:
        return sqrt_helper(n,int_min,guess-1)

# Essentially binary search to get the answer => O(logn)
