# fibonacci with memoization
# common way to optimize exponential time recursive algos
from typing import List

def printFibs(n: int) -> List[int]:
    # create list called `memo` of length n to cache results
    memo = [0] * n
    for i in range(n):
        print(f"{i}: {fib(i, memo)}")

def fib(n: int, memo: List[int]) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # memo default values are 0s, so check if the value for the nth fib number has already been computed
    elif memo[n] > 0:
        return memo[n]

    # "else block" b/c we'd already have returned if we went into prev blocks
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

printFibs(15)

# Time complexity
# with the memoization, we get the value for fib(i) just by doing an O(1) lookup to the previous two values and summing
# this means we are doing a constant amount of work n times => O(n)

# Space complexity
# the trade off with memoization is obviously space, we cache results in array O(n)
