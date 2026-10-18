
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    char_count = Counter(s)
    freq_count = Counter(char_count.values())

    # All characters appear the same number of times
    if len(freq_count) == 1:
        return "YES"

    # More than two different frequencies cannot be fixed
    # by removing just one character
    if len(freq_count) > 2:
        return "NO"

    # Check the two different frequencies
    (freq1, count1), (freq2, count2) = freq_count.items()

    # One character occurs only once; remove that character
    if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
        return "YES"

    # One frequency is exactly one greater and occurs once
    if freq1 == freq2 + 1 and count1 == 1:
        return "YES"

    if freq2 == freq1 + 1 and count2 == 1:
        return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
