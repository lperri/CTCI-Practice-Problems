# check if a number is prime by checking for divisibility on numbers less than it.
# only need to go up to SQRT(n) because if n is divisble by a number greater than its SQRT,
# then it is divisible by something smaller than it.
from math import sqrt

def is_prime(n: int) -> bool:
    ''' Use while loop '''
    x = 2
    while x <= sqrt(n):
        if n % x == 0:
            return False
        x += 1
    return True

# def is_prime(n: int) -> bool:
#     '''
#     Use for loop:
#     key #1 is to convert sqrt(n) to int -- if prime, won't be an int!
#     key #2 is to make sure to +1 to the end of the range, otherwise
#         range(2,2) if n=4 => returns True, wrong!
#     '''
#     for x in range(2, int(sqrt(n))+1):
#         print('x: ', x)
#         if n % x == 0:
#             return False
#     return True

print(is_prime(4))
print('4: ', is_prime(4))
print('7: ', is_prime(7))
print('36: ', is_prime(36))
print('17: ', is_prime(17))

# time complexity: O(SQRT(n))