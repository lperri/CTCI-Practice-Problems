# The following code computes the product of a and b. What is its runtime?

def product(a,b):
    sum = 0
    # note that I will use xrange here to take O(constant) memory
    for i in xrange(b):
    # note that range and xrange are [inclusive,exclusive) and "start" argument is by default 0 if unspecified also the third optional argument is the stepsize
        sum += a
    return sum

""" the answer: the runtime of this code is O(b) """
        
