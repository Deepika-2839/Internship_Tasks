
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s1 and STRING s2 as parameters.
#

def makingAnagrams(s1, s2):
    count = 0

    for char in set(s1 + s2):
        count += abs(s1.count(char) - s2.count(char))

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()
    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
