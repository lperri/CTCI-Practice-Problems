# compute the Nth fibonacci number

# The Fibonacci Sequence is the series of numbers:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# The next number is found by adding up the two numbers before it:
# the 2 is found by adding the two numbers before it (1+1),
# the 3 is found by adding the two numbers before it (1+2),
# the 5 is (2+3),
# and so on!

def fib(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# Time complexity O(2^n), O(n) space on callstack

# Bonus:
# What is the time complexity for a function that prints all fib numbers from 0 to n
# i.e. for loop that calls fib(n) n times
#
# answer is NOT O(n2^n) -> Write out tree of calls -- look for maximum depth (could expand out F2, F1 more but not max)
#
# For Fibonacci recursive implementation or any recursive algorithm,
# the space required is proportional to the maximum depth of the recursion tree,
# because, that is the maximum number of elements that can be present
# in the implicit function call stack.
#
#            F6
#       /          \
#      F5          F4
#     / \          / \
#   F4   F3      F3   F2
#  / \   / \    / \
# F3 F2 F2 F1  F2 F1
# / \
# F2 F1
# /\
# F1 F0
#
# clearly, the depth is proportional to N => the depth of the callstack is N
# for time, this is also consistent: O(branches^depth) = O(2^N)
