# URLify: write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold extra chars
# and that you are given the "true" length of the string.

# clarifying Q: should we care about special chars? -> assume no, keep them

def urlify_string(string: str) -> str:
    string_array = list(string)
    j = len(string_array) - 1
    i = j
    # place i at the last non-space char of the string
    while string_array[i] == " ":
        i -= 1
    while i >= 0:
        if string_array[i] == " " and string_array[j] == " ":
            # insert %20 here
            string_array[j-2], string_array[j-1], string_array[j] = "%", "2", "0"
            i, j = i - 1, j - 3
        # swap with the space char indexed by j
        else:
            string_array[i], string_array[j] = string_array[j], string_array[i]
            i -= 1
            j -= 1
    return "".join(string_array)

# time complexity O(s), space O(s)

if __name__ == "__main__":
    string = "Mr John Smith    "
    string2 = "Oh hey Leah Perri! That's you, right?            "
    print(urlify_string(string))
    print(urlify_string(string2))