# Problem: Nested Lists
# HackerRank Link: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    second_lowest = sorted(set([s for n, s in records]))[1]
    names = sorted([n for n, s in records if s == second_lowest])
    for n in names:
        print(n)
