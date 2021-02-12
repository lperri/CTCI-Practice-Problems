# string compression: implement a function to perform basic string compression  using the counts of repeated characters
# for ex. : "aabcccccaaa" would become "a2b1c5a3"
# assume string has only uppercase and lowercase letters

def string_compression(string: str) -> str:
    if not string:
        return
    # optimization from just concatenating strings -- O(n^2) -> O(n)
    compressed_string_list = []

    prev_char = string[0]
    i, char_count = 1, 1
    while i < len(string):
        char = string[i]
        if char == prev_char:
            char_count += 1
        else:
            compressed_string_list.append(prev_char + f"{char_count}")
            char_count = 1
        i += 1
        prev_char = char

    # need to handle final character(s) outside of while loop
    compressed_string_list.append(prev_char + f"{char_count}")

    return "".join(compressed_string_list)


if __name__ == "__main__":
    str_to_compress1 = "aaabbcccdefggggaaa"
    str_to_compress2 = "a"
    print(string_compression(str_to_compress1))