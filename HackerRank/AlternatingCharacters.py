#!/bin/python

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    # start at the end of the string
    i = len(s) - 1
    num_del = 0
    while i > 0:
        if s[i-1] == s[i]:
            new_s = s[:i-1]+s[i:]
            num_del += 1
            s = new_s
        i -= 1
    return num_del

#print 'answer to the example "ABBABAAA" should be 3'
#print alternatingCharacters('ABBABAAA')

#print 'answer to the example "ABBABAAABB" should be 4'
#print alternatingCharacters('ABBABAAABB')
