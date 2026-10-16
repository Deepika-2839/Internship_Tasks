# Problem: sWAP cASE
# HackerRank Link: https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    result = ""
    for c in s:
        if c.islower():
            result += c.upper()
        elif c.isupper():
            result += c.lower()
        else:
            result += c
    return result

if __name__ == '__main__':
    s = input()
    print(swap_case(s))
