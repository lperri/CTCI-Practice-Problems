# compute n factorial using recursion
# n! = n*(n-1)*(n-2)*(n-3)...
# factorial is only defined for non-negative numbers => return -1 if n < 0
# also recall 0! = 1

def factorial(n: int) -> int:
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))

# Time complexity: O(n) -- requires O(n) recursive calls
# Space complexity: O(n) recursive calls in stack