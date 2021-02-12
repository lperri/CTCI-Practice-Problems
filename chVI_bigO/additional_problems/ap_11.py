# the following code prints all strings of length k where the characters are in sorted oder. It does this by generating all strings of length k and checking if each is sorted. what is runtime?
import string

"""
Examples for generateString():

    Input: set = {'a', 'b'}, k = 3

    Output:
    aaa
    aab
    aba
    abb
    baa
    bab
    bba
    bbb
    ----------------------------------------------
    Input: set = {'a', 'b', 'c', 'd'}, k = 1

    Output:
    a
    b
    c
    d

checkSorted will then return T/F depending on if string is sorted
=> we only want sorted strings, so if checkSorted evaluates to T
"""

class PrintAllKLengthStrings:

    """
        Print all strings of length k where the characters are in sorted order.
        We could do this in two separate steps like:
            1. Generate all strings of length k
            2. Check if each is sorted
        But this seems inefficient.

        We could check at each decision point whether or not our constraint
        (sorted property) remains valid. If it does, we accept decision to add the letter.
        Otherwise we reject and choose another letter.

        So the general algorithm is to:
            1. Choose next character from char_set and add to prefix
            2. Check if string is still sorted
            3. If it is valid, recurse there -- fill the next (k - [filled]) slots
            4. If invalid, reject choice, backtrack to previous prefix

        Base case:
        - We have created a string of length k -- add to set and return!
    """

    def __init__(self, k: int, char_set: set):
        # turn char_set into a list so that it can be indexed
        self.char_set_list = list(char_set)
        self.sorted_strings_list = set()
        # call sortedStrings automatically
        self.generateString(k)

    def generateString(self, k: int, prefix: str = ''):

        # base case k = 0, finished the string
        if k == 0:
            print(prefix)
            self.sorted_strings_list.add(prefix)
            prefix = ''
            return

        for i, char in enumerate(self.char_set_list):
            # this is the sorted constraint -- next char must be >= last one
            # if i == 0, no need to worry about this
            if (i == 0) or (i > 0 and (char >= self.char_set_list[i - 1])):
                prefix += char
                # k decrements by 1 because we have added a new char to prefix
                self.generateString(k - 1, prefix)

# runtime: O(c^k) -- O(branches^depth) -- where k is the length of the string and c is the number of characters in the set
# Note: this is a combination problem NchooseX - backtracking

if __name__ == "__main__":
    PrintAllKLengthStrings(2, {'a', 'b'})