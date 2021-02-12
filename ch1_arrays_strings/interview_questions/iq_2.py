# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation(string1: str, string2: str) -> bool:
    char_dict_string1, char_dict_string2 = {}, {}

    def _populate_dict(string: str, char_dict: dict) -> None:
        for char in string:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    _populate_dict(string1, char_dict_string1)
    _populate_dict(string2, char_dict_string2)

    return char_dict_string1 == char_dict_string2

# time complexity of above solution: O(s1 + s2), space O(s1 + s2)
# alternatively could sort both strings O(s1logs1 + s2logs2) time and O(s1 + s2) space


if __name__=="__main__":
    perm_string1, perm_string2 = "lollapalooza", "zoolaapallol"
    print(check_permutation(perm_string1, perm_string2))
    not_perm_string1, not_perm_string2 = "banana", "bananna"
    print(check_permutation(not_perm_string1, not_perm_string2))
