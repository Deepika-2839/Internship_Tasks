# Problem: String Split and Join
# HackerRank Link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # split on space and join with hyphen
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
