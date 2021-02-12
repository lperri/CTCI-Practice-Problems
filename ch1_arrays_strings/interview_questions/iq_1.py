# Is Unique: implement an alogirthm to determine if a string has all unique chars
# what if you can't use additional data structures?

# clarifying questions:
# can we assume only lowercase alphabetic (a-z) characters in string (26)? --> the issue with this case is we'd need to
# use a hash map to map all 26 chars to a number...
# UNLESS you know this:  Each lower case letter is in the range 97-122 (26 characters.)
# So, if you just subtract 96 from the ordinal of any lower case letter, you will get its position in the alphabet assuming you take 'a' == 1.

# if not, ASCII (128)? Extended ASCII (256)? Unicode (143,859)?

def is_unique(string: str) -> bool:
    """
        Naive implementation is use a set or dict
        O(s) runtime and O(s) space where s is the length of the string
        However, based on response to clarifying Q, we can cap the number of
        possible chars... => Could argue that it is O(1)!
    """
    return len(set(string)) == len(string)

def is_unique(string: str) -> bool:
    """
        Another implementation is use a boolean array
        O(s) runtime and O(1) space where s is the length of the string.
        We could also argue time complexity is O(1) if we have a fixed
        char set.

        Number of unique chars depends on response to clarifying Q,
        Would affect size of boolean array -- for simplicity, say 256.

        The key here is knowing the built-in ord() function returns ASCII value
        (int) of a string -- (side note: you can also convert back to char
        usiing chr() function.)
    """
    char_was_seen = [False]*256
    for char in string:
        if char_was_seen[ord(char)]:
            return False
        char_was_seen[ord(char)] = True
    return True

def is_unique(string: str) -> bool:
    """
        If no other data structure can be used, will have to make tradeoff in time comp
        We could either compare every char to every other char O(n^2) or
        modify original string by sorting it (O(nlogn)) time.
    """
    prev_char = ''
    for char in sorted(string):
        if char == prev_char:
            return False
        prev_char = char
    return True


if __name__ == "__main__":
    string_not_unique = "hello"
    string_unique = "code"
    print(is_unique(string_not_unique))
    print(is_unique(string_unique))
