# Problem: Nested Lists
# HackerRank Link: https://www.hackerrank.com/challenges/nested-list/problem

n = int(input())
students = []
for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(list(set([s[1] for s in students])))
second_lowest = scores[1]

result = []
for name, score in students:
    if score == second_lowest:
        result.append(name)

result.sort()
for name in result:
    print(name)
