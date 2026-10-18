
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    stack = []

    for char in s:
        # Check whether the last character matches the current character
        if stack and stack[-1] == char:
            stack.pop()
        else:
            # Add the character if it does not match
            stack.append(char)

    # If all characters are removed
    if not stack:
        return "Empty String"

    # Convert the remaining characters into a string
    return "".join(stack)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
