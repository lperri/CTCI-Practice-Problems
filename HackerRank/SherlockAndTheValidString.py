#!/bin/python

import math
from collections import Counter

def isValid(s):
    char_counts = Counter(s)
    if len(set(char_counts.values())) == 1:
        # all chars have same number of occurances
        return 'YES'
    elif len(set(char_counts.values())) > 2:
        # at least 3 chars have different number of occurances
        return 'NO'
    else:
        max_occ = max(char_counts.values())
        min_occ = min(char_counts.values())

        return 'YES'

print 'Enter a string: '
s = raw_input().strip()
result = isValid(s)
print result
