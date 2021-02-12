# palindrome permutation: write a function to check if a string is a permutation of a palindrome

# the defining property of a palindrome that I will check is that it must have no more than 1 char
# that appears an odd number of times -- all other chars must appear an even number of times
#

def is_permutation_palindrome(string: str) -> bool:
    char_dict = {}

    # populate char_dict
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    # count number of chars that appear odd number of times
    num_odd = 0
    for char in char_dict:
        if num_odd > 1:
            return False
        if char_dict[char] % 2 != 0:
            num_odd += 1
    return True

if __name__ == "__main__":
    pal_string = "arceacr"
    non_pal_string ="dooolll"
    print(is_permutation_palindrome(pal_string))
    print(is_permutation_palindrome(non_pal_string))
