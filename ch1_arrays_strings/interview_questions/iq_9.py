# string rotation: assume you have a method is_substring which checks if one word is a substring of
# another. Given two strings, s1 and s2, check if s2 is a rotation of s1 using oonyl one call to
# is_substring

# a rotated string has one pivot point: example - waterbottle / erbottewat
# so the question is there a way we can make s1 (xy) into s2 (yx)?
# we can check if the xy in yxyx=y(xy)x is equal to s1, i.e. if s1 is a substring of s2s2

def is_substring(s1: str, s2: str) -> bool:
    return s1 in s2

def is_string_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return is_substring(s1, s2 + s2)

if __name__ == "__main__":
    print(is_string_rotation('waterbottle', 'erbottlewat'))
    print(is_string_rotation('waterbottle', 'erbottwattt'))
    print(is_string_rotation('waterbottle', 'erbott'))