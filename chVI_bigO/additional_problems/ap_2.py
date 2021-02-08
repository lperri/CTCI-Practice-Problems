# the following code computes a^b. What is its runtime?

def power(a,b):
    if b < 0:
        print 'running through it 1x'
        return 0
    elif b == 0:
        print 'running through it 1x'
        return 1
    else:
        print 'runnning through it 1x'
        return a*power(a,(b-1))

""" THE ANSWER TO MY QUESTION!!! 
for a recursive function even when each call is O(1), you have to think about the number of calls to that function that are made. O(b)
"""

# notes: 
# - it makes b+1 run throughs before getting to the answer.
