# one way: there are three types of edits that can be performed on strings: insert a char, remove a char, replace a char
# given two strings, write a function to check if they are one edit or zero edits away

def _create_and_populate_char_dict(string: str) -> dict:
    char_dict =  {}
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def _get_number_of_differences(string1_dict: dict, string2_dict: dict) -> int:
    number_differences = 0
    for key in string1_dict:
        if key not in string2_dict:
            number_differences += string1_dict[key]
        elif string1_dict[key] != string2_dict[key]:
            number_differences += abs(string1_dict[key] - string2_dict[key])
    return number_differences

def _check_insertion_removal_replacement(string1: str, string2: str, string1_dict: dict, string2_dict: dict) -> bool:
    # first condition correponds to insertion or removal; second corresponds to replacement
    # one of the conditions must be true
    if (abs(len(string1) - len(string2)) != 1) and (len(string1) != len(string2)):
        return False
    number_differences = _get_number_of_differences(string1_dict, string2_dict)
    if number_differences > 1:
        return False
    return True

def check_one_way(string1: str, string2: str) -> bool:
    # zero edits case
    if string1 == string2:
        return True
    # one edits case
    string1_dict, string2_dict = \
        _create_and_populate_char_dict(string1), _create_and_populate_char_dict(string2)
    return (
        _check_insertion_removal_replacement(string1, string2, string1_dict, string2_dict)
    )


if __name__ == "__main__":
    insert_or_removal_string1, insert_or_removal_string2 = "plac", "place"
    replacement_string1, replacement_string2 = "cake", "bake"
    zero_edits_string1, zero_edits_string2 = "flew", "flew"
    false_string1, false_string2 = "pale", "bake"
    print(
        "true: ", check_one_way(insert_or_removal_string1, insert_or_removal_string2),
        "true: ", check_one_way(replacement_string1, replacement_string2),
        "true: ", check_one_way(zero_edits_string1, zero_edits_string2),
        "false: ", check_one_way(false_string1, false_string2)

    )
