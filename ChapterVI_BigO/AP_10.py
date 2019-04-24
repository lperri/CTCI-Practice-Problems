# the following code sums the digits in a number. what is its runtime?

def sumDigits(n):
    sum = 0
    while n > 0:
        sum += (n % 10)
        n /= 10
    return sum

""" you cut the problem space / 10 each time you loop, so this is log(base10)n, or b/c base doesn't matter for Big O, logn.
"""

