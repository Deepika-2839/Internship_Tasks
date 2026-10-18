#!/bin/python3

from collections import Counter

if __name__ == '__main__':
    s = input()

    count = Counter(s)
    result = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    for char, frequency in result[:3]:
        print(char, frequency)

