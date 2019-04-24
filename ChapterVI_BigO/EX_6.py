# reverse array

example_array_1 = [1,2,3,4]
example_array_2 = [3,4,6,7,9,10,11,15,14]

def reverseArray(array):
    """ takes an array and reverses all elements """
    i = 0
    N = len(array)
    while i < N/2:
        current = array[i]
        element_to_swap = array[N-i-1]
        array[i] = element_to_swap
        array[N-i-1] = current
        i += 1
    return array

print 'example array 1 is: ',example_array_1
print 'result of reversal: ',reverseArray(example_array_1)
print 'example array 2 is: ',example_array_2
print 'result of reversal: ', reverseArray(example_array_2)


# points of this ex: 
# - don't forget the -1 in the array index for the element_to_swap!
# - understand that you MUST iterate only through N/2 elements, otherwise you will un-reverse it!
# - N/2 takes care of the odd-length arrays because the middle number remains in position!
