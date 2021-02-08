# The appendToNew method appends a value to an array by creating a new, longer array and returning this longer array. You've used the appendToNew method to create a copyArray function that repeatedly calls appendToNew. How long does copying an array take?

""" important notes about Java:
    int[] arrayObject = new int[5]
    ^^ this will declare an array of integers, size 5
    how to declare an array variable in Java is just type[] name = new type[size]
                                                  OR int intArray[];
                                                  OR int[] intArray;

"""

# this whole exercise doesn't really apply to python bc mem allocation but....

def copyArray(array):
    copy = []
    for value in array:
        copy = appendToNew(copy, value)
    return copy

def appendToNew(array, value):
    """ copy all elements over to new array """
    bigger = [0]*(len(array)+1)
    
    for i in xrange(len(array)):
        bigger[i] = array[i]
   
    bigger[len(array)]=value
    return bigger


print copyArray([1,2,3,4,5])

""" calling copyArray varies depending on the size of copy, which changes each time appendToNew is called by one; --> O(1+2+3...+n) ~ O(n^2) """



