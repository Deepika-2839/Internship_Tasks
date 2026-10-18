
from collections import Counter

def gameOfThrones(s):
    # Count the frequency of each character
    freq = Counter(s)

    # Count how many characters have an odd frequency
    odd_count = 0

    for count in freq.values():
        if count % 2 != 0:
            odd_count += 1

    # A palindrome can have at most one odd frequency
    if odd_count <= 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    s = input().strip()
    result = gameOfThrones(s)
    print(result)
