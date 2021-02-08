# the following code prints all strings of length k where the characters are in sorted oder. It does this by generating all strings of length k and checking if each is sorted. what is runtime?

""" things learned:
    - method overloading: the compiler will know to direct a call to a method that has the same name as another method based on the number of arguments passed
    - in python, you can do optional parameters when defining a method """

class FunWithStrings(object):

    """ prints all possible sorted strings for a given number of letters, which CTCI refers to as k """

    def __init__(self, number_letters):
        self.remaining = number_letters

    def ithLetter(self, character):
        return (string.ascii_lowercase).find(character)
    
    def printSortedStrings(self, remaining, prefix=''):
        if remaining == 0:
            if self.isInOrder(prefix):
                print prefix
        else:
            for character in string.ascii_lowercase:
                printSortedStrings(remaining-1,prefix+character)


    def isInOrder(self, string):
        isInOrder = True
        for i in xrange(1,len(string)):
            prev = self.ithLetter(i-1)
            curr = self.ithLetter(i)
            if prev > curr:
                isInOrder = False
        return isInOrder

testing_obj = FunWithStrings('hello')
print testing_obj.printSortedStrings(7) 
